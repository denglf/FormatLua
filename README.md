## Summary

FormatLua formats lua code to a more readable form by using [Lua Development Tools library](https://github.com/eclipse/koneki.ldt/tree/master/libraries).


## How to Use

* Select lua code and click menu Selection -> Format -> Format Lua Code
* Select lua code and press super+k, super+l

### Configure setting
Setting lua path in FormatLua.sublime-settings

```json
{
    "lua_path": "/usr/local/bin/lua"
}
```
### Configure key binding

Add the following line to keymap settings

```json
{ "keys": ["super+k", "super+l"], "command": "format_lua" }
```

## Support for Sublime Text 3
* Install FormatLua from Package Control.
* Open `Installed Packages` directory, copy `FormatLua.sublime-package` to `Packages` directory and rename to `FormatLua.zip`.
* Unzip `FormatLua.zip` to `Packages` and remove `FormatLua.zip`.

## Example

Original:

```lua
local a = "你好"
    local b
    function set_text(name, value)
            local doc = document:getElementsByName(name)
        if doc and #doc > 0 then
        doc[1]:setPropertyByName("text", value)
    end
    end
    return b
```
Formated:

```lua
local a = "你好"
local b
function set_text(name, value)
    local doc = document:getElementsByName(name)
    if doc and #doc > 0 then
        doc[1]:setPropertyByName("text", value)
    end
end
return b
```
