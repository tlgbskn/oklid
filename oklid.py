import math

# Noktaların tanımlanması
points = [(1, 2), (4, 6), (5, 9), (2, 3), (8, 1)]

# Öklid mesafesi için fonksiyon tanımlama
def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

# Mesafelerin hesaplanması
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        dist = euclideanDistance(points[i], points[j])
        distances.append(dist)

# Minimum mesafenin bulunması
min_distance = min(distances)

print("Mesafeler: ", distances)
print("Minimum Mesafe: ", min_distance)
