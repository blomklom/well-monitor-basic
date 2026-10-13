WELL_NAME = "Скважина № 101"
FIELD_NAME = "Ромашкинское"
DEPTH_M = 2500
DAILY_RATE_T = 35
WELL_STATUS = "В эксплуатации"

def main():
    print("=== ПАСПОРТ НЕФТЯНОЙ СКВАЖИНЫ ===")
    print(f"Название: {WELL_NAME}")
    print(f"Месторождение: {FIELD_NAME}")
    print(f"Глубина: {DEPTH_M} м")
    print(f"Суточная добыча: {DAILY_RATE_T} т")
    print(f"Статус: {WELL_STATUS}")

if __name__ == "__main__":
    main()
