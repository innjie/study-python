class ThailandPackage:
    def detail(self):
        print("Thailand package")


if __name__ == "__main__" :
    print("Thailand 직접실행")
    trip_to = ThailandPackage()
    trip_to.detail()
else:
    print("외부 호출")