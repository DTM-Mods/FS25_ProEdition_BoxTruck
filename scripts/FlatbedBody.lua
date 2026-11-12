-- PropaineX flatbed: optional Universal Autoload default loading area.
-- X (side walls + tailgate, or stakes) uses the game's Foldable specialization; this script handles no keys.
FlatbedBody = {}
FlatbedBody.MOD_NAME = g_currentModName
FlatbedBody.SPEC_NAME = g_currentModName .. ".flatbedBody"

function FlatbedBody.prerequisitesPresent(specializations)
    return true
end

function FlatbedBody.initSpecialization()
    -- Kept so saves from 1.4.0.0 (separate tailgate key) still validate; the value is no longer used.
    Vehicle.xmlSchemaSavegame:register(XMLValueType.BOOL,
        "vehicles.vehicle(?)." .. FlatbedBody.SPEC_NAME .. "#tailgateOpen", "Unused since 1.4.0.1", false)
end

function FlatbedBody.registerEventListeners(vehicleType)
    SpecializationUtil.registerEventListener(vehicleType, "onPreLoad", FlatbedBody)
end

function FlatbedBody.getUal(self)
    for i, class in pairs(self.specializations or {}) do
        local name = (self.specializationNames or {})[i]
        if type(name) == "string" and name:sub(-#".universalAutoload") == ".universalAutoload" then return class end
    end
end

function FlatbedBody:onPreLoad(savegame)
    local ual = FlatbedBody.getUal(self)
    if ual == nil or ual.VEHICLE_CONFIGURATIONS == nil or ual.OPTIONS_DEFAULTS == nil or ual.LOADING_AREA_DEFAULTS == nil then return end
    local name = self.configFileName
    if type(name) ~= "string" then return end
    if g_modsDirectory ~= nil and name:sub(1, #g_modsDirectory) == g_modsDirectory then name = name:sub(#g_modsDirectory + 1) end
    -- Ours replaces whatever the settings file has for this truck (an older build saved 2.38 m there, too narrow
    -- for two pallets sideways), same as the box truck.
    local config = {selectedConfigs = ual.ALL or "ALL"}
    for _, item in ipairs(ual.OPTIONS_DEFAULTS) do if item.id ~= nil then config[item.id] = item.default end end
    local area = {}
    for _, item in ipairs(ual.LOADING_AREA_DEFAULTS) do if item.id ~= nil then area[item.id] = item.default end end
    -- Stakes project inward from the deck edge; use their clear width for both bodies.
    area.offset, area.width, area.length, area.height = {0, 1.625, -1.925}, 2.44, 6.70, 2.20
    config.loadArea = {area}
    ual.VEHICLE_CONFIGURATIONS[name] = {[config.selectedConfigs] = config}
    FlatbedBody.hookPickupZones(ual)
end

-- Pallet pickup zones the same size as the Krone ProfiLiner's (user, 2026-11-12: "when I pull up to load pallets,
-- I'm getting all of them that are on the ground that a ProfiLiner can get"). UAL sizes the side pickup zones from
-- the load area (length + width/2, 3 x height); our deck is 6.70 m, the ProfiLiner's 13.40 m x 2.50 m high, so ours
-- only reached about half as far. Only the side zones are resized, centred on the load area, and only on our two
-- trucks (flatbed, and the box truck: user, 2026-11-12 "for the box truck too, the same loading area"; BoxTruckBody
-- calls this too). The load areas themselves stay real. All sizes are the ProfiLiner's own (UAL default 2.44 x 2.50
-- x 13.4), so both trucks get exactly its zone.
FlatbedBody.PROFILINER = {width = 2.44, length = 13.4, height = 2.50}
FlatbedBody.PICKUP_SPECS = {"spec_" .. FlatbedBody.SPEC_NAME, "spec_" .. g_currentModName .. ".boxTruckBody"}
function FlatbedBody.isOurTruck(vehicle)
    for _, key in ipairs(FlatbedBody.PICKUP_SPECS) do if vehicle[key] ~= nil then return true end end
    return false
end
function FlatbedBody.hookPickupZones(ual)
    if ual.flatbedProPickupHooked or type(ual.updateLoadingTriggers) ~= "function" then return end
    ual.flatbedProPickupHooked = true
    local original = ual.updateLoadingTriggers
    ual.updateLoadingTriggers = function(vehicle, ...)
        local result = original(vehicle, ...)
        local spec = vehicle.spec_universalAutoload
        if FlatbedBody.isOurTruck(vehicle) and spec ~= nil and spec.triggers ~= nil and spec.loadVolume ~= nil then
            local d = 2 * (ual.TRIGGER_DELTA or 0.1)
            local w = FlatbedBody.PROFILINER.width
            local width = (spec.extendPickupRange and 3 or 1.66) * w
            local height = 3 * FlatbedBody.PROFILINER.height
            local length = FlatbedBody.PROFILINER.length + w / 2
            local tx = 1.1 * (width + w) / 2
            for id, x in pairs({leftPickupTrigger = tx, rightPickupTrigger = -tx}) do
                local trigger = spec.triggers[id]
                if trigger ~= nil and trigger.node ~= nil then
                    setScale(trigger.node, width - d, height - d, length - d)
                    setTranslation(trigger.node, x, 0, 0)
                    local sx, sy, sz = getScale(trigger.node)
                    trigger.sizeX, trigger.sizeY, trigger.sizeZ = width, height, length
                    trigger.width, trigger.height, trigger.length = width / sx, height / sy, length / sz
                    trigger.offset = {x, 0, 0}
                end
            end
        end
        return result
    end
end
