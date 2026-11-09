-- Review only (scratch copy): flatbed widened from 2.48 to ~2.85 m outside, 3 goat-milk pallets across.
local data='G:/SteamLibrary/steamapps/common/Farming Simulator 25/data/'
local SHIFT=0.185                     -- each side moves out this much
local K=(1.24+SHIFT)/1.24             -- width factor for the centred deck parts
local function find(n,name)
 if getName(n)==name then return n end
 for i=0,getNumOfChildren(n)-1 do local r=find(getChildAt(n,i),name); if r then return r end end
end
local root=getRootNode()
local comp=find(root,'fh16_main_component1')
local body=find(comp,'flatbedBody')

-- hide gizmos (lights/cameras) so the shots are clean
local function hideGizmos(n)
 if getHasClassId(n,ClassIds.LIGHT_SOURCE) then setVisibility(n,false) end
 for i=0,getNumOfChildren(n)-1 do hideGizmos(getChildAt(n,i)) end
end
hideGizmos(root)

WCAM=WCAM or createCamera('WideReviewCamera',math.rad(36),.05,500); link(root,WCAM)
function wideView(px,py,pz,tx,ty,tz,fov)
 setTranslation(WCAM,px,py,pz); setDirection(WCAM,px-tx,py-ty,pz-tz,0,1,0)
 setFovY(WCAM,math.rad(fov or 36)); setCamera(WCAM); clearSelection()
end

function wideSides(which)   -- 'stakes' or 'boards'
 setVisibility(find(body,'OPTION_STAKES'),which=='stakes')
 setVisibility(find(body,'OPTION_BOARDS'),which=='boards')
end

local palletFile
local function pallet()
 if not palletFile then
  palletFile=loadI3DFile(data..'objects/pallets/goatMilkCanPallet/goatMilkCanPallet.i3d',false,false,false)
  local p=getChildAt(palletFile,0)
  local wf=loadI3DFile(data..'objects/pallets/shared/euroPallet/euroPallet.i3d',false,false,false)
  local w=getChildAt(wf,0); link(p,w); setTranslation(w,0,0,0); delete(wf)
  unlink(p); PALLETPROTO=p; setVisibility(p,false); link(root,p)
 end
 local c=clone(PALLETPROTO,false,false,false); setVisibility(c,true); return c
end

function wideLoad(xs)
 if LOADGROUP then delete(LOADGROUP) end
 LOADGROUP=createTransformGroup('Wide_review_load'); link(comp,LOADGROUP)
 for layer=0,1 do for row=0,4 do for _,x in ipairs(xs) do
  local p=pallet(); link(LOADGROUP,p)
  setTranslation(p,x,1.625+layer*.98,.675-row*1.30); setRotation(p,0,math.pi/2,0)
 end end end
 print(string.format('[WIDE] loaded %d pallets (%d across x5 x2)',#xs*10,#xs))
end

function wideApply()
 setScale(find(body,'Flatbed_FIXED'),K,1,1)
 for _,n in ipairs({'flatbedColFloor','flatbedColHeadboard','flatbedTailgate'}) do
  local nd=find(body,n); local sx,sy,sz=getScale(nd); setScale(nd,sx*K,sy,sz)
 end
 for _,g in ipairs({'OPTION_STAKES','OPTION_BOARDS','flatbedBelts'}) do
  local grp=find(body,g)
  for i=0,getNumOfChildren(grp)-1 do
   local c=getChildAt(grp,i)
   if getName(c)~='flatbedTailgate' then
    local x,y,z=getTranslation(c); if math.abs(x)>0.5 then setTranslation(c,x+(x>0 and SHIFT or -SHIFT),y,z) end
   end
  end
 end
 -- belts: end node is a child offset along local z; recompute nothing (preview only)
 print(string.format('[WIDE] applied: centred parts x%.4f, sides +/-%.3f m; rails at +/-%.3f',K,SHIFT,1.24+SHIFT))
end

wideSides('stakes')
wideLoad({-.475,.475})
wideView(7.5,4.2,-12,0,2.1,-1.6,36)
