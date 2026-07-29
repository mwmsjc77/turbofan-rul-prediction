# Previsão de Vida Útil de Motores (NASA Turbofan)

Projeto de ETL e análise exploratória usando o dataset CMAPSS da NASA, 
que simula dados de sensores de motores turbofan até o momento de falha.

## Objetivo
Calcular o RUL (Remaining Useful Life) de cada motor com base em dados 
de sensores ao longo dos ciclos de operação — base para futuros modelos 
de manutenção preditiva.

## Fonte dos dados
[NASA Turbofan Jet Engine Data Set (CMAPSS)](https://www.kaggle.com/datasets/behrad3d/nasa-cmaps) — Kaggle

## Etapas
- [x] Carregar e nomear colunas do dataset
- [x] Checar valores nulos e tipos de dados
- [x] Calcular RUL por motor
- [x] Remover sensores sem variação
- [x] Salvar dataset tratado em Parquet
- [x] Gráfico de degradação de sensor

## Tecnologias
Python, Pandas

## Como rodar
```bash
```