import subprocess
import toml
import re

if __name__ == '__main__':
    tests = toml.load("conf.toml")
    args = tests['application']
    encoding = tests['encoding']
    for test in tests['testSuite']:
        process = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        input = test['input']
        output = test['output']
        data = process.communicate(bytes(input, encoding))[0]
        out = data.decode("866")
        regular = re.compile(output, re.ASCII)
        if regular.match(out) is not None:
            print("Тест " + str(test['number']) + " пройден")
        else:
            print("Тест " + str(test['number']) + " не пройден")
            print("Ожидаемый результат: " + output + "\nРезультат работы: " + out)
