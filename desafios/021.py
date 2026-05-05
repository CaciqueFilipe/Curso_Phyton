# Faça um programa que abra e reproduza o áudio de um arquivo mp3.

import pygame
import os

# Nome do arquivo que deve estar na mesma pasta ou o caminho completo
arquivo = 'Caminho do arquivo na maquina'

pygame.mixer.init()
if os.path.exists(arquivo):
    pygame.mixer.music.load(arquivo)
    pygame.mixer.music.play()
    input('Reproduzindo áudio... Pressione ENTER para parar.')
else:
    print(f'Erro: O arquivo "{arquivo}" não foi encontrado no diretório.')

'''
## Correção sugerida pelo Gustavo:

import pygame

print("\n{:=^20}".format(" Gustavo "))

pygame.init()
pygame.mixer.music.load('audio.mp3')
pygame.mixer.music.play()
pygame.event.wait()

'''