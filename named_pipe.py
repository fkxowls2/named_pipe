import win32file, win32pipe
import numpy as np

class NamedPipe:
    def __init__(self):
        pass
    
    def client_build(self):
        try:
            self.client = win32file.CreateFile(
                "\\\\.\\pipe\\cshap_python", 
                win32file.GENERIC_READ | win32file.GENERIC_WRITE, #desiredAccess 
                0, #shareMode
                None, #attributes 
                win32file.OPEN_EXISTING, #CreationDisposition 
                0, #flagsAndAttributes
                None  #hTemplateFile
            )
        except:
            print('파이프가 연결되었는지 확인하세요.')
        else:
            print('파이프가 연결되었습니다.')
    
    def read_byte(self, byte_length=248161078):
        _, img_byte = win32file.ReadFile(self.client, byte_length)
        self.img_byte = img_byte

        return self.img_byte
    
    def get_img_arr(self, info_length=1078, reshape_size=(15000, 16544)):
        buffer = np.frombuffer(self.img_byte, np.uint8)[info_length:]
        img_arr = buffer.reshape(reshape_size)
        self.img_arr = np.flipud(img_arr)
        
        return self.img_arr
    
    def server_build(self, byte_length=248161078):
        self.server = win32pipe.CreateNamedPipe(
            r'\\.\pipe\cshap_python', 
            win32pipe.PIPE_ACCESS_DUPLEX, 
            win32pipe.PIPE_TYPE_MESSAGE | win32pipe.PIPE_READMODE_MESSAGE | win32pipe.PIPE_WAIT, 
            1, #nMaxInstances
            byte_length, byte_length, #nOutBufferSize, nInBufferSize
            0, None)  #nDefaultTimeOut, _win32typing.PySECURITY_ATTRIBUTES
        
        print('파이프 서버가 생성되었습니다.')
        win32pipe.ConnectNamedPipe(self.server, None)
        
    def write_byte(self, byte_data):
        err, bytes_written = win32file.WriteFile(self.server, byte_data)
        print(err, bytes_written)
        win32file.FlushFileBuffers(self.server)
        
    def server_close(self):
        win32pipe.DisconnectNamedPipe(self.server)
        win32file.CloseHandle(self.server)