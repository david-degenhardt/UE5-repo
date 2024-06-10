import matplotlib.pyplot as plt


# Sortiert die "input_list" mit Merge Sort
def merge_sort(input_list):
    
    if (len(input_list) > 1):

        # Teilung der Liste in 2 Hälften.
        middle = len(input_list) // 2
        left_half = input_list[:middle]
        right_half = input_list[middle:]

        # Rekursive sortierung beider Hälften.
        merge_sort(left_half)
        merge_sort(right_half)

        left_index = 0
        right_index = 0
        merge_index = 0

        # Vergleiche die Elemente der beiden (sortierten)Hälften und merge das Ergebnis zurück in die Liste.
        while left_index < len(left_half) and right_index < len(right_half):
            if left_half[left_index] <= right_half[right_index]:
                input_list[merge_index] = left_half[left_index]
                left_index += 1
            else:
                input_list[merge_index] = right_half[right_index]
                right_index += 1
            merge_index += 1

        # Kopieren von verbleidenden Elementen der linken Hälfte
        while left_index < len(left_half):
            input_list[merge_index] = left_half[left_index]
            left_index += 1
            merge_index += 1

        # Kopieren von verbleidenden Elementen der rechten Hälfte
        while right_index < len(right_half):
            input_list[merge_index] = right_half[right_index]
            right_index += 1
            merge_index += 1



list_to_sort = [54, 26, 93, 17, 77, 31, 44, 55, 20]

# Plot der unsortierten Liste
x = range(len(list_to_sort))
plt.bar(x, list_to_sort, align='center', alpha=0.5)
plt.title('Unsortierte Liste')
plt.xlabel('Index')
plt.ylabel('Wert')
plt.show()


merge_sort(list_to_sort)

# Plot der sortierten Liste
x = range(len(list_to_sort))
plt.bar(x, list_to_sort, align='center', alpha=0.5)
plt.title('Sortierte Liste')
plt.xlabel('Index')
plt.ylabel('Wert')
plt.show()