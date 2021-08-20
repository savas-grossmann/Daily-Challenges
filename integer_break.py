"""
https://leetcode.com/problems/integer-break/

Die Faktoren belaufen sich auf 2 und 3. 1 wird elimiert, da es unnötig ist und keinen Gewinn bringt.
Alles >= 4 wird elimiert, da es durch 2 und 3 ersetzt werden kann.
Das heißt wenn wir einen Faktor f haben der >= 4 ist, ersetzen wir diesen durch 2*(f-2) da dies immer >= f.
Des Weiteren haben wir maximal 2 mal die 2 drin, weil wenn wir mehr als 2 2en haben, zum Beispiel 2*2*2
können wir dies durch 3*3 ersetzen und kommen auf mehr Gewinn am Ende. Wir wollen also so viele 3en wie möglich nutzen.
"""


def integer_break(n):
    if n == 2 or n == 3:
        return n - 1
    elif n % 3 == 0:
        return pow(3, n / 3)
    elif n % 3 == 1:
        return 4 * pow(3, (n - 4) / 3)
    else:
        return 2 * pow(3, (n - 2) / 3)


if __name__ == '__main__':
    print(integer_break(10) == 36)
