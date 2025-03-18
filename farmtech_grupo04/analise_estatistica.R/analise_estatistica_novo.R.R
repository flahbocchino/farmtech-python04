# Instalar pacotes (execute apenas na primeira vez)
install.packages("httr")
install.packages("jsonlite")
install.packages("readr")

# Carregar bibliotecas
library(httr)
library(jsonlite)
library(readr)

# 📂 Carregar os dados do CSV gerado pelo Python
dados <- read_csv("data/plantio.csv")

# Verificar a estrutura dos dados
print(dados)

# 📊 Cálculo estatístico
media_area <- mean(dados$Área)
desvio_padrao_area <- sd(dados$Área)

cat("\n📊 Estatísticas das Áreas Plantadas 📊\n")
cat("Média da Área Plantada:", media_area, "m²\n")
cat("Desvio Padrão da Área Plantada:", desvio_padrao_area, "m²\n")

# 🌤️ Conectar-se à API meteorológica
api_key <- "SUA_CHAVE_AQUI"  # Substitua pela sua chave da OpenWeatherMap
cidade <- "São Paulo"
url <- paste0("https://api.openweathermap.org/data/2.5/weather?q=", cidade, "&appid=", api_key, "&units=metric")

resposta <- GET(url)
dados_clima <- fromJSON(content(resposta, "text"))

# Extração dos dados climáticos
temperatura <- dados_clima$main$temp
sensacao_termica <- dados_clima$main$feels_like
umidade <- dados_clima$main$humidity
descricao <- dados_clima$weather[[1]]$description

cat("\n🌤️ Informações Meteorológicas 🌤️\n")
cat("Cidade:", cidade, "\n")
cat("Temperatura Atual:", temperatura, "°C\n")
cat("Sensação Térmica:", sensacao_termica, "°C\n")
cat("Umidade:", umidade, "%\n")
cat("Condições Climáticas:", descricao, "\n")
setwd("C:/Users/flahb/OneDrive/Documentos/farmtech_grupo04")
source("analise_estatistica.R")
dados <- read.csv("C:/Users/flahb/OneDrive/Documentos/farmtech_grupo04/plantio.csv", 
                  stringsAsFactors = FALSE, 
                  sep = ",", 
                  fileEncoding = "UTF-8")


