"""Rolador de dados D&D. Execute: python dice_roller.py 2d20kh1+5"""
import argparse
import json
import re
import secrets

PATTERN = re.compile(r"^(\d{1,3})d(4|6|8|10|12|20|100)(kh1|kl1|dl1)?([+-]\d+)?$", re.I)

def roll(expression):
    expr = expression.replace(" ", "").lower()
    match = PATTERN.fullmatch(expr)
    if not match:
        raise ValueError("Formato inválido. Ex.: 1d20+5, 2d20kh1, 4d6dl1")
    count, sides, mode, modifier = match.groups()
    count, sides, modifier = int(count), int(sides), int(modifier or 0)
    if not 1 <= count <= 100:
        raise ValueError("Quantidade deve ser de 1 a 100")
    if mode and count < 2:
        raise ValueError("Manter/descartar exige pelo menos dois dados")
    rolls = [secrets.randbelow(sides) + 1 for _ in range(count)]
    kept = list(range(count))
    if mode == "kh1":
        kept = [max(range(count), key=lambda i: rolls[i])]
    elif mode == "kl1":
        kept = [min(range(count), key=lambda i: rolls[i])]
    elif mode == "dl1":
        removed = min(range(count), key=lambda i: rolls[i])
        kept = [i for i in range(count) if i != removed]
    total = sum(rolls[i] for i in kept) + modifier
    return {"expression": expr, "rolls": rolls, "kept_indices": kept,
            "modifier": modifier, "total": total}

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("expression", help="Ex.: 1d20+5, 2d20kh1, 4d6dl1")
    args = parser.parse_args()
    try:
        print(json.dumps(roll(args.expression), ensure_ascii=False))
    except ValueError as error:
        parser.error(str(error))
