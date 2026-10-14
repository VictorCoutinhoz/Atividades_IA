import cv2

imagem = cv2.imread("imagem_entrada.jpg")

if imagem is None:
    print("erro ao carregar imagem")
else:
    print("dimensoes: ", imagem.shape)

    altura, largura = imagem.shape[:2]
    lado = min(altura, largura)
    y = (altura - lado) // 2
    x = (largura - lado) // 2
    recorte = imagem[y:y + lado, x:x + lado].copy()

    # mantém o azul e zera verde e vermelho.
    recorte[:, :, 1] = 0
    recorte[:, :, 2] = 0

    cv2.namedWindow("original", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("original", 800, 600)
    cv2.moveWindow("original", 20, 20)

    cv2.namedWindow("ROI azul", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("ROI azul", 400, 400)
    cv2.moveWindow("ROI azul", 850, 20)

    imagem_menor = cv2.resize(imagem, (600, 600))
    recorte_menor = cv2.resize(recorte, (400, 400))

    cv2.imshow("original", imagem_menor)
    cv2.imshow("ROI azul", recorte_menor)

    cv2.imwrite("resultado_roi.png", recorte)
    print("resultado_roi.png")

    cv2.waitKey(0)
    cv2.destroyAllWindows()