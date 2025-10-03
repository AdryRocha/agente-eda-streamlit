import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
from langchain.tools import Tool

class EDAToolkit:
    """Uma caixa de ferramentas para Análise Exploratória de Dados que encapsula o DataFrame."""
    
    def __init__(self, df: pd.DataFrame):
        """Inicializa a caixa de ferramentas com o DataFrame a ser analisado."""
        self.df = df
        os.makedirs("plots", exist_ok=True)

    def get_dataset_overview(self, query: str = "") -> str:
        """Fornece uma visão geral do dataset."""
        info = [
            f"Dimensões do Dataset: {self.df.shape[0]} linhas x {self.df.shape[1]} colunas\n",
            "Tipos de Dados:\n" + str(self.df.dtypes) + "\n",
            "\nInformações sobre Valores Nulos:\n" + str(self.df.isnull().sum()) + "\n",
            "\nPrimeiras 5 linhas do Dataset:\n" + str(self.df.head())
        ]
        return "\n".join(info)

    def get_descriptive_statistics(self, query: str = "") -> str:
        """Retorna estatísticas descritivas do dataset."""
        return str(self.df.describe())

    def get_column_value_counts(self, column_name: str) -> str:
        """Retorna contagem de valores únicos em uma coluna."""
        if column_name not in self.df.columns:
            return f"Erro: Coluna '{column_name}' não encontrada no dataset."
        return str(self.df[column_name].value_counts().head())

    def plot_histogram(self, column_name: str) -> str:
        """Gera histograma de uma coluna."""
        try:
            if column_name not in self.df.columns:
                return f"Erro: Coluna '{column_name}' não encontrada."
            
            plt.figure(figsize=(10, 6))
            plt.hist(self.df[column_name], bins=30)
            plt.title(f'Histograma de {column_name}')
            plt.xlabel(column_name)
            plt.ylabel('Frequência')
            
            filename = f"plots/histogram_{column_name}.png"
            plt.savefig(filename)
            plt.close()
            
            return f"Histograma salvo como {filename}"
        except Exception as e:
            return f"Erro ao criar histograma: {str(e)}"

    def plot_correlation_heatmap(self, query: str = "") -> str:
        """Gera mapa de calor de correlações."""
        try:
            plt.figure(figsize=(12, 8))
            sns.heatmap(self.df.corr(), annot=True, cmap='coolwarm', fmt='.2f')
            plt.title('Mapa de Calor de Correlações')
            
            filename = "plots/correlation_heatmap.png"
            plt.savefig(filename)
            plt.close()
            
            return f"Mapa de calor salvo como {filename}"
        except Exception as e:
            return f"Erro ao criar mapa de calor: {str(e)}"

    def plot_scatter(self, columns: str) -> str:
        """Gera gráfico de dispersão entre duas colunas."""
        try:
            col1, col2 = map(str.strip, columns.split(','))
            
            if col1 not in self.df.columns or col2 not in self.df.columns:
                return f"Erro: Uma ou ambas as colunas não encontradas no dataset."
            
            plt.figure(figsize=(10, 6))
            plt.scatter(self.df[col1], self.df[col2], alpha=0.5)
            plt.title(f'Gráfico de Dispersão: {col1} vs {col2}')
            plt.xlabel(col1)
            plt.ylabel(col2)
            
            filename = f"plots/scatter_{col1}_vs_{col2}.png"
            plt.savefig(filename)
            plt.close()
            
            return f"Gráfico de dispersão salvo como {filename}"
        except Exception as e:
            return f"Erro ao criar gráfico de dispersão: {str(e)}"

    def get_tools(self) -> list:
        """Retorna lista de ferramentas para o agente."""
        return [
            Tool(
                name="Visão Geral do Dataset",
                func=lambda x="": self.get_dataset_overview(x),
                description="Obtém visão geral do dataset, incluindo forma, tipos de dados e valores nulos"
            ),
            Tool(
                name="Estatísticas Descritivas",
                func=lambda x="": self.get_descriptive_statistics(x),
                description="Calcula estatísticas descritivas para colunas numéricas"
            ),
            Tool(
                name="Contagem de Valores",
                func=lambda x: self.get_column_value_counts(x),
                description="Conta frequência de valores únicos em uma coluna específica"
            ),
            Tool(
                name="Histograma",
                func=lambda x: self.plot_histogram(x),
                description="Gera histograma para visualizar distribuição de uma coluna numérica"
            ),
            Tool(
                name="Mapa de Calor de Correlação",
                func=lambda x="": self.plot_correlation_heatmap(x),
                description="Cria mapa de calor mostrando correlações entre variáveis numéricas"
            ),
            Tool(
                name="Gráfico de Dispersão",
                func=lambda x: self.plot_scatter(x),
                description="Gera gráfico de dispersão entre duas colunas numéricas. Formato: 'coluna1, coluna2'"
            )
        ]