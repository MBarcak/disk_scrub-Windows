#include <stdio.h>
#include <Windows.h>
#include <winbase.h>
#include <tchar.h>
#include <stdint.h>

extern "C" __declspec(dllexport) void func1(const char* Disk) {
	char szDriver[MAX_PATH] = { 0 };
	::wsprintf(szDriver, "\\\\.\\%s:", Disk);
	HANDLE hdisk = ::CreateFile(szDriver, GENERIC_READ | GENERIC_WRITE, FILE_SHARE_READ | FILE_SHARE_WRITE, NULL, OPEN_EXISTING, 0, NULL);
	if (hdisk == INVALID_HANDLE_VALUE) {
		printf("CreateFile错误, 返回!\n");
		printf("%d\n", GetLastError());
	}

	DISK_GEOMETRY dg = { 0 };
	BOOL bResult1 = FALSE;
	BOOL bResult2 = FALSE;
	DWORD junk = 0;
	
	bResult1 = ::DeviceIoControl(hdisk,
		IOCTL_DISK_GET_DRIVE_GEOMETRY,
		NULL,
		0,
		&dg,
		sizeof(dg),
		&junk,
		NULL);
	if (bResult1 == FALSE)
	{
		printf("无法获得磁盘大小,返回!\n");
		return;
	}

	int BytePerSector = (ULONG)dg.BytesPerSector;  //每扇区字节数
	DWORD64 qwFreeBytesToCaller = 0, qwTotalBytes = 0, qwFreeBytes = 0;
	char Driver[3]="\0";
	sprintf(Driver, "%s:", Disk);
	bResult2 = ::GetDiskFreeSpaceEx(Driver,
		(PULARGE_INTEGER)&qwFreeBytesToCaller,
		(PULARGE_INTEGER)&qwTotalBytes,
		(PULARGE_INTEGER)&qwFreeBytes);
	
	if (bResult2 == FALSE)
	{
		printf("无法获得扇区数,返回!\n");
		return;
	}
	
	//std::cout << qwTotalBytes << std::endl;
	//std::cout << BytePerSector << std::endl;
	long long int sectors = qwTotalBytes/BytePerSector;  //总扇区数
	//std::cout << sectors_to_scan << std::endl;

	printf("Start... \n");
	
	BOOL ok = FALSE;
	// 卸载请求显式锁定卷
	ok = ::DeviceIoControl(hdisk, FSCTL_DISMOUNT_VOLUME, NULL, 0, NULL, 0, NULL, NULL);
	if (FALSE == ok)
	{
		printf("卸载请求显式锁定卷失败,返回!\n");
		return;
	}
	int p;
	int q=1;
	for (p = 0; p < sectors; ++p) {
		LARGE_INTEGER position = { p * 512 };
		ok = FALSE;
		ok = ::SetFilePointerEx(hdisk, position, NULL, FILE_BEGIN);
		BYTE buffer[512];
		memset(buffer, 0, 512);
		ok = ::WriteFile(hdisk, buffer, 512, NULL, NULL);
		if (ok == FALSE)
		{
			printf("磁盘擦写错误,返回!\n");
			return;
		}
		if (p == (sectors / 100)*q)  //显示进度
		{
			printf("%d%%\n", q);
			q++;
		}
	}
	
	::CloseHandle(hdisk);
	return;
}

