"""โปรแกรมตรวจสอบบัตรประชาชน"""
def main():
    """รับค่ารหัสประจำตัวประชาชน"""
    Id = input()
    if len(Id) == 13:
        print("yes")
    else:
        print("no")
main()
