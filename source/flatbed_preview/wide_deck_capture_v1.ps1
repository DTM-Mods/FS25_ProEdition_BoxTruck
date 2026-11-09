$ErrorActionPreference='Stop'
$T="C:\Users\groov\OneDrive\Documents\My Games\FarmingSimulator2025\MOD PROJECTS\Library\_FS25Knowledge\tools\ge10"
. "$T\ui.ps1"
$out=(Resolve-Path "$PSScriptRoot/../../previews/flatbed_wide_v1").Path
$lua=(Resolve-Path "$PSScriptRoot/wide_deck_v1.lua").Path
& "$T\mockup\ge_open.ps1" "$env:LOCALAPPDATA\Temp\claude\fbw\flatbedTruck.i3d" @($lua)
Start-Sleep 3
$views=@{rear34='wideView(7.5,4.2,-12,0,2.1,-1.6,36)';rear='wideView(0,2.6,-15,0,2.1,-3,30)';top='wideView(0.01,15,-1.0,0,1.6,-2.0,40)'}
function Shot($name,$code){
 $f=Join-Path $out ($name+'.lua'); Set-Content $f $code
 Click 1000 1320; Send '^a'; Paste ('source("'+$f.Replace('\','/')+'")'); Send '+{ENTER}'; Start-Sleep 2
 Click 1000 1320; Send '^a'; Paste ('source("'+$f.Replace('\','/')+'")'); Send '+{ENTER}'; Start-Sleep 2
 & "$T\mockup\cap.ps1" (Join-Path $out ($name+'.png'))
}
foreach($v in 'rear34','rear','top'){ Shot "before_$v" $views[$v] }
Shot 'after_apply' "wideApply()`nwideLoad({-.92,0,.92})`n$($views.rear34)"
foreach($v in 'rear34','rear','top'){ Shot "after_$v" $views[$v] }
Shot 'after_boards_rear34' "wideSides('boards')`n$($views.rear34)"
