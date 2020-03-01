# coding=utf-8
import os
import shutil


def move_suportfiles(files, root_path="./"):
    for file in files:
        shutil.copy("./" + file, root_path + "/" + file)


def package_python_file(filepath, distpath="./"):
    """
    :param filepath: the python file path you want to package
    :param distpath: the output dir path
    :return:
    """
    if len(filepath.split(".")) < 2 or filepath.split(".")[-1] != "py":
        raise RuntimeError("please input right format")
    else:
        command = r"pyinstaller -Dw {filepath} --distpath {distpath} --clean".format(filepath=filepath,
                                                                                     distpath=distpath)
        os.system(command)


def move_file_of_py_installer_by_tree(root_path, dll_names, exclude_files=None):
    """
    :param root_path: the path you want to clean
    :param dll_names: the dll name list
    :param exclude_file: a list with exclude filename
    :return: none
    """
    executor_name = root_path.split("/")[-1] + ".exe"
    # tasklist / m | more
    base_files = dll_names + ['base_library.zip',
                              'image_register.exe',
                              'image_register.exe.manifest']
    if exclude_files:
        base_files = base_files + exclude_files
    base_files += [executor_name]
    for root, dirs, files in os.walk(root_path):
        for file in files:
            if file not in base_files:
                old_path = os.path.join(root, file)
                os.remove(old_path)
                print(old_path, "had been remove")
    print("dir redundant is cleaned")


def main():
    file_name = "realtime"
    # tasklist / m | more
    dll_names = ['ntdll.dll', 'KERNEL32.DLL', 'KERNELBASE.dll', 'USER32.dll', 'win32u.dll', 'GDI32.dll',
                 'gdi32full.dll', 'msvcp_win.dll', 'ucrtbase.dll', 'WS2_32.dll', 'RPCRT4.dll', 'IMM32.DLL',
                 'python36.dll', 'SHLWAPI.dll', 'msvcrt.dll', 'combase.dll', 'bcryptPrimitives.dll', 'VERSION.dll',
                 'ADVAPI32.dll', 'sechost.dll', 'VCRUNTIME140.dll', 'CRYPTBASE.DLL', 'CRYPTSP.dll', 'rsaenh.dll',
                 'bcrypt.dll', '_ctypes.pyd', 'ole32.dll', 'OLEAUT32.dll', '_socket.pyd', 'select.pyd', '_bz2.pyd',
                 '_lzma.pyd', 'pyexpat.pyd', '_hashlib.pyd', 'win32api.pyd', 'SHELL32.dll', 'cfgmgr32.dll',
                 'shcore.dll', 'windows.storage.dll', 'profapi.dll', 'powrprof.dll', 'UMPDC.dll', 'kernel.appcore.dll',
                 'pywintypes36.dll', 'secur32.dll', 'SSPICLI.DLL', 'pythoncom36.dll', 'uxtheme.dll', 'urlmon.dll',
                 'iertutil.dll', 'cv2.cp36-win_amd64.pyd', 'COMDLG32.dll', 'COMCTL32.dll', 'AVIFIL32.dll',
                 'AVICAP32.dll', 'MSVFW32.dll', 'WINMM.dll', 'WINMMBASE.dll', 'MFPlat.DLL', 'MF.dll', 'MFReadWrite.dll',
                 'MSACM32.dll', 'MFCORE.DLL', 'CRYPT32.dll', 'MSASN1.dll', 'ksuser.dll', 'RTWorkQ.DLL',
                 'multiarray.cp36-win_amd64.pyd', 'mkl_rt.dll', 'umath.cp36-win_amd64.pyd',
                 'lapack_lite.cp36-win_amd64.pyd', '_umath_linalg.cp36-win_amd64.pyd', '_decimal.pyd',
                 '_mklinit.cp36-win_amd64.pyd', 'fftpack_lite.cp36-win_amd64.pyd', '_pydfti.cp36-win_amd64.pyd',
                 'multiarray_tests.cp36-win_amd64.pyd', 'mtrand.cp36-win_amd64.pyd', 'CompPkgSup.DLL', 'clbcatq.dll',
                 'Windows.Media.dll', 'ntmarta.dll', 'FSClient.dll', 'dxgi.dll', 'MFSENSORGROUP.dll', 'd3d11.dll',
                 'dxcore.dll', 'Windows.ApplicationModel.dll', 'twinapi.appcore.dll', 'RMCLIENT.dll', 'AVRT.dll',
                 'AppXDeploymentClient.dll', 'StateRepository.Core.dll', 'vidcap.ax', 'kswdmcap.ax', 'MFC42.dll',
                 'Windows.StateRepositoryPS.dll', 'WinTypes.dll', 'mfx_mft_mjpgvd_64.dll', 'PROPSYS.dll',
                 'mfmjpegdec.dll', 'mfperfhelper.dll', 'msvproc.dll', 'OpenCL.dll', 'IntelOpenCL64.dll',
                 'intelocl64.dll', 'task_executor64.dll', 'cpu_device64.dll', 'igdrcl64.dll', 'igdgmm64.dll',
                 'igdfcl64.dll', 'igc64.dll', 'nvopencl.dll', 'SETUPAPI.dll', 'nvfatbinaryLoader.dll', 'DEVOBJ.dll',
                 'WINTRUST.dll', 'nvapi64.dll', 'MSCTF.dll', 'TextInputFramework.dll', 'CoreMessaging.dll',
                 'CoreUIComponents.dll']
    support_files = ["haarcascade_frontalface_default.xml"]
    package_python_file("./{name}.py".format(name=file_name))
    move_suportfiles(support_files, "./{name}".format(name=file_name))
    move_file_of_py_installer_by_tree("./{name}".format(name=file_name), dll_names, support_files)


if __name__ == '__main__':
    main()
