# first enable execution of scripts with the following command
# set-executionpolicy remotesigned

$ida_plugins_dir = "$env:APPDATA\Hex-Rays\IDA Pro\plugins"
$plugin_dirs = @(
    "IDASkins\plugins"
    "AMIE"
    "keypatch"
)

# clean the existing plugins folder
if (Test-Path -Path $ida_plugins_dir) {
    Remove-Item -Recurse -Path "$ida_plugins_dir" | Out-Null
}
New-Item -ItemType directory -Path "$ida_plugins_dir" | Out-Null

# copy the plugins
foreach ($p in $plugin_dirs) {
    Copy-Item -Recurse ".\$p\*" -Destination "$ida_plugins_dir"
}
