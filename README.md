# My dotfiles
## Demo

![Demo](https://media.discordapp.net/attachments/886507265450991617/1054282160141504512/filename_12_19_131808.png)

With all the file from this repo in your `.config` folder, everything should look the same as the demo picture except the wallpaper can be found [here](https://wallhaven.cc/w/m3dm1k).

---

## Read this before use

### Alacritty

I'm using konsole as main terminal and alacritty to display float terminal. If you're using alacritty as main, then the config will be slightly different. Maybe replacing alacritty in my config with another resizing-supported terminal will work.

### Fonts

Has been added in to `fonts` folder, but you also can download it on [Nerd Font Homepage](https://www.nerdfonts.com/font-downloads).

### I3 config file

There're some `bindsym` options to launch programs installed on **my** computer. I don't know using the config file without installing those programs will return any error but make sure to check all `bindsym` and remove unnecessary lines.

This is **i3-gaps** config file. Until i3 and i3-gaps be merge together, you won't be able to use this on i3-wm. Removing `gaps` options is also a way, but the bar won't work correctly.

### Picom

Try to change the blur method if *gaussian* doesn't work on your computer.

### Polybar

I'm getting some issues with the wifi module. All `Wifi Disconnected Icons` and `Wifi Ramp Signal Icons` Fontawsome icons doesn't display even I'm using a solid fontawsome font for the wifi bar. I'll try to fix it asap.

[^1]: Send me a message on [my twitter](https://twitter.com/0ji54n) if you get any other issue. 
