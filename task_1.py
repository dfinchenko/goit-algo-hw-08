import heapq

def min_cost_to_connect_cables(cable_lengths):
    total_cost = 0
    
    # Створюємо мінімальну купу з довжин кабелів
    heapq.heapify(cable_lengths)

    while len(cable_lengths) > 1:
        # Вилучаємо два кабелі з найменшою довжиною
        first = heapq.heappop(cable_lengths)
        second = heapq.heappop(cable_lengths)
        
        # Сумуємо їх довжини та додаємо до загальних витрат
        cost = first + second
        total_cost += cost
        
        # Додаємо новий кабель (суму довжин) назад до купи
        heapq.heappush(cable_lengths, cost)
    
    return total_cost

# Довжини кабелів
cable_lengths = [5, 4, 2, 8]
min_cost = min_cost_to_connect_cables(cable_lengths)

print(f"Мінімальні загальні витрати на об'єднання кабелів становлять: {min_cost}")