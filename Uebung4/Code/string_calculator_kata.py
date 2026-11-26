#implementiert von: JYBS, RTRE

# TODO: Implementiere den String Calculator mit TDD
# Hinweise: Beginne mit den Basisregeln ("" -> 0, "1" -> 1, "1,2" -> 3)
# Erweitere schrittweise mit Tests für \n, benutzerdefinierte Delimiter, etc.

def add(numbers: str) -> int:
    # TODO: Implementierung
    if numbers == "":
        return 0

    numbers = numbers.replace("\n", ",")
    numbers = numbers.replace("/",",")
    numbers = numbers.replace(";",",")

    for char in numbers:
        if not (char.isdigit() or (char == "-") or (char == ",")):
                return "Ungültige Eingabe."

    if "," in numbers:
        nums = numbers.split(",")
        result = 0
        index = 0
        for num in nums:
            if num == "":
                num = 0
            if num == "-":
                num = 0
                nums[index+1] = nums[index+1]*(-1)
            result += int(num)
            index += 1
        return result

    return int(numbers)

