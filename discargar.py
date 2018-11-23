#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, sys, json, time

niveles = 2

categorias = open("categorias","r")

resultados = {}


def getRelatedWords(palabrita):
    os.system('wget "http://relatedwords.org/api/related?term='+ palabrita +'" -O temporalis.json')
    
    with open('temporalis.json') as fileJson:
        data = json.load(fileJson)

    return data

for categoria in categorias:
    resultados[categoria] = []

    data =  getRelatedWords(categoria)

    print("Actual: "+ categoria + '**************************************************\n')

    for i in data:
        # print(i["word"])

        while(True):
            try:
                x = raw_input(i["word"] + ' (y/n/h): ')
            except UnicodeEncodeError:
                x = 'n'

            if(x == 'y' or x == 'n' or x == 'h'):
                break

        if(x == 'n'):
            continue

        elif(x == 'h'):
            resultados[categoria].append(i["word"])
            continue

        resultados[categoria].append(i["word"])

        dataPerLevel = getRelatedWords(i["word"])

        for pal in dataPerLevel:
            resultados[categoria].append(pal["word"])

    with open('resultados/'+categoria.replace('\n',''), 'w') as outFile:
        for valor in resultados[categoria]:
            try:
                outFile.write(valor+'\n')
            except UnicodeEncodeError:
                continue


