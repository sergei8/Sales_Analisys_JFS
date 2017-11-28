#!/usr/bin/env python
# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt


class Order:
    """
    Класс содержит методы для визуализации  различных характеристик датафрейма 'orders'
    """
    
    def __init__(self, df):
        self.orders = df
    
    # вывод частотной гистограммы показателей датафрейма
    def futures_dist(self, y_max=0, y_min=0):
        # f, (ax1, ax2) = plt.subplots(2)
        # y = orders.SA_HDR_TIC.count() - orders.count().values    # значения по шкале `y`
        y = self.orders.count().values  # значения по шкале `y`
        
        N = len(y)  # всего колонок в диаграмме  = длине списка `y`
        x = range(N)  # упорядоченый счетик колонок [0: N-1]
        names = list(self.orders.count().index)  # наименования колонок по оси `x`
        # plt.figure(figsize=(7,5))
        
        plt.bar(x, y)  # рисуем barchart
        plt.xticks(x, names, rotation='vertical')  # подписываем колонкы на оси `x`
        plt.ylim(min(y) - y_min, max(y) + y_max)  # показать `верхушку` диаграммы
        plt.show()


