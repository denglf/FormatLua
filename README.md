## Summary

FormatLua formats lua code to a more readable form by using [Lua Development Tools library](https://github.com/eclipse/koneki.ldt/tree/master/libraries).


## How to Use

Select lua and click menu Selection -> Format -> Format Lua Code

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
