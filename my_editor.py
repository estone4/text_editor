import menus.menu_sys
import startup

# Determine OS
if "win" == startup.sys.platform[:3]:
    startup.style.theme_use('vista')
elif "darwin" in startup.sys.platform:
    startup.style.theme_use('clam')
else:
    startup.style.theme_use('clam')

bg = startup.style.lookup("TLabel", "background")
startup.root.configure(bg=bg)
# -------------------------------------------------------------------------------

startup.root.config(menu=startup.menu)

startup.textPad.pack()

startup.root.mainloop()
