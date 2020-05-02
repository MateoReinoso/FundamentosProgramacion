def resulHanoi(disk, origen, medio, destino):
    if disk >= 1:
        resulHanoi(disk-1, origen, destino, medio)
        print("Mover disco de Torre", origen, "a", destino)
        resulHanoi(disk-1, medio, origen, destino)
resulHanoi(3, 1, 2, 3)