# first enable execution of scripts with the following command
# set-executionpolicy remotesigned

$ida_dir = "$env:APPDATA\Hex-Rays\IDA Pro"

$ida_plugins_dir = "${ida_dir}\plugins"
$ida_themes_dir = "${ida_dir}\themes"

$plugin_dirs = @(
    "AMIE"
    "IDASkins\plugins"
    "keypatch"
)
$theme_dirs = @(
    "themes\vscode-dark"
)

# clean the existing plugins and themes folders
if (Test-Path -Path $ida_plugins_dir) {
    Remove-Item -Recurse -Path "$ida_plugins_dir" | Out-Null
}
if (Test-Path -Path $ida_themes_dir) {
    Remove-Item -Recurse -Path "$ida_themes_dir" | Out-Null
}

# make new plugins and themes folders
New-Item -ItemType directory -Path "$ida_plugins_dir" | Out-Null
New-Item -ItemType directory -Path "$ida_themes_dir" | Out-Null

# copy the plugins
#foreach ($p in $plugin_dirs) {
#    Copy-Item -Recurse ".\$p\*" -Destination "$ida_plugins_dir"
#}

# copy the themes
foreach ($p in $theme_dirs) {
    Copy-Item -Recurse ".\$p" -Destination "$ida_themes_dir"
}
