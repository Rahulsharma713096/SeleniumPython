# define doctor class
class Doctor:
    def __init__(self, dId, dName, spec, sonFee):
        self.dId = dId
        self.dName = dName
        self.spec = spec
        self.sonFee = sonFee


# define Hospital class
class Hospital:
    def __init__(self, doctorOB):
        self.doctorOB = doctorOB

    def sDBN(self, reqDoctorName):
        doclist = []
        for i in self.doctorOB.values():
            if i.dName == reqDoctorName:
                doclist.append(i)
        return doclist

    def cCFS(self, reqsep):
        fee = 0
        for i in self.doctorOB.values():
            if i.spec == reqsep:
                fee = fee + i.sonFee
        return fee


if __name__ == '__main__':
    doctorOB = {}
    count = int(input())
    for i in range(count):
        doctorId = int(input())
        doctorName = input()
        spec = input()
        consultation = int(input())
        doctorObj = Doctor(doctorId, doctorName, spec, consultation)
        doctorOB[doctorId] = doctorObj
    hospital = Hospital(doctorOB)
    reqDoctorName = input()
    reqSpec = input()
    dolist = hospital.sDBN(reqDoctorName)
    if dolist == []:
        print("No doctor exit with the given name")
    else:
        for i in dolist:
            print(i.dId)
            print(i.dName)
            print(i.spec)
            print(i.sonFee)
    fee = hospital.cCFS(reqSpec)
    if fee != 0:
        print(fee)
    else:
        print("NO Doctor with given  specilation")

'''
5
9091
GovindRaju
ENT
500
99002
Madhuri
Dermatokogict
700
90903
Oiva
Gynaeclogist
600
90984
Suryam
Cardiologist
900
9095
Madhuri
Cardiologist
1000
Madhuri
Cardiologist  '''
