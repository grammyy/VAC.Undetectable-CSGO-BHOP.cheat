import keyboard,pymem,ctypes

try:
    p,user32=pymem.Pymem("csgo.exe"),ctypes.windll.user32
    client,engine=pymem.pymem.process.module_from_name( p.process_handle, "client.dll" ).lpBaseOfDll,pymem.pymem.process.module_from_name( p.process_handle, "engine.dll" ).lpBaseOfDll
    player=p.read_uint( client + 14398924 )
    def GetWindowText(handle, length=100):
        window_text = ctypes.create_string_buffer(length)
        user32.GetWindowTextA(handle,ctypes.byref(window_text),length)
        return window_text.value
    def GetForegroundWindow():
        return user32.GetForegroundWindow()
    while True :
        if GetWindowText(GetForegroundWindow()).decode('cp1252')=="Counter-Strike: Global Offensive - Direct3D 9":
            if client and engine and p:
                player = p.read_uint( client + 14398924 )
            if keyboard.is_pressed( "space" ):
                force_jump = client + 86514276
                on_ground = p.read_uint( player + 260 )
                if player and on_ground == 257 or on_ground == 263:
                    p.write_int( force_jump, 6 )
except KeyboardInterrupt:
    pass
except:
    print("csgo.exe wasn't available; please open csgo.exe first.")