import string
import random 
import traceback
from parser import keyMiner, checkIfValidHelm
from scanner import isValidUserName, isValidPasswordName, isValidKey

def fuzzValues():
    randomValue = random.randint(-100, 100)
    randomLetters = ''.join(random.choices(string.ascii_letters, k = 10))
    return randomValue, randomLetters



def Fuzzer():
    with open("fuzz_report.txt", "w") as report:
        for i in range(10): 
            fuzzedInt, fuzzedStr = fuzzValues()

            try:
                isValidUserName(fuzzedStr)
                isValidUserName(fuzzedInt)
                isValidUserName(Null)
               ## isValidPasswordName(fuzzedStr)
               ## checkIfValidHelm(fuzzedStr)
               ## isValidKey(fuzzedInt)
               ## keyMiner(fuzzedINt, fuzzValues)
                report.write(f"Iterations {i}:isValidUserName Success\n")
            except Exception as e:
                Error = traceback.format_exception(type(e),e,e.__traceback__)
                report.write(f"Iteration {i}:isValidUserName Failed - {''.join(Error)}\n")
                
            else:
                report.write("fuzzing isValidUserName done!\n")

            try:
               ## isValidUserName(fuzzedStr)
                isValidPasswordName(fuzzedStr)
                isValidPasswordName(fuzzedInt)
               ## checkIfValidHelm(fuzzedStr)
               ## isValidKey(fuzzedInt)
               ## keyMiner(fuzzedINt, fuzzValues)
                report.write(f"Iterations {i}:isValidPasswordName Success\n")
            except Exception as e:
                ## Error = traceback.format_exception(etype = type(e), value = e, tb =e.__traceback__)
                Error1 = traceback.format_exception(type(e),e,e.__traceback__)
                report.write(f"Iteration {i}:isValidPasswordName Failed- {''.join(Error1)}\n")
                
            else:
                report.write("fuzzing for isValidPasswordName done!\n")

            try:
               ## isValidUserName(fuzzedStr)
               ## isValidPasswordName(fuzzedStr)
                checkIfValidHelm(fuzzedStr)
                checkIfValidHelm(fuzzedInt)
               ## isValidKey(fuzzedInt)
               ## keyMiner(fuzzedINt, fuzzValues)
                report.write(f"Iterations {i}:checkIfValidHelm Success\n")
            except Exception as e:
                Error2 = traceback.format_exception(type(e),e,e.__traceback__)
                report.write(f"Iteration {i}:checkIfValidHelm Failed- {''.join(Error2)}\n")
                
            else:
                report.write("fuzzing for checkIfValidHelm done!\n")
            try:
               ## isValidUserName(fuzzedStr)
               ## isValidPasswordName(fuzzedStr)
               ## checkIfValidHelm(fuzzedStr)
                isValidKey(fuzzedStr)
                isValidKey(fuzzedInt)
               ## keyMiner(fuzzedINt, fuzzValues)
                report.write(f"Iterations {i}: isValidKey Success\n")
            except Exception as e:
                Error3 = traceback.format_exception(type(e),e,e.__traceback__)
                report.write(f"Iteration {i}: isValidKey Failed- {''.join(Error3)}\n")
                
            else:
                report.write("fuzzing for isvalidKey done!\n")
            try:
               ## isValidUserName(fuzzedStr)
               ## isValidPasswordName(fuzzedStr)
               ## checkIfValidHelm(fuzzedStr)
               ## isValidKey(fuzzedInt)
                keyMiner(fuzzedINt, fuzzValues)
                report.write(f"Iterations {i}: KeyMiner passed\n")
            except Exception as e:
                Error4 = traceback.format_exception(type(e),e,e.__traceback__)
                report.write(f"Iteration {i}: KeyMiner Failed- {''.join(Error4)}\n")
                break
            else:
                report.write("fuzzing for KeyMiner done!\n")
if __name__ == '__main__':
    Fuzzer()



