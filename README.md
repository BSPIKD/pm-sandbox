# interactions.py šablona

[//]: # (todo dodělat všude url url)
**Tento kód není spustitelný bez `předchozí úpravy` a repositáře [pm-core]()**

Je potřeba aby bot běžel na verzi `python 3.8.6`, kterou
stáhnete [zde](https://www.python.org/downloads/release/python-386/). 
---
## Instalace

### Klon repositáře

 šablonu použijete pomocí tlačítka, které je nahoře 
 
![image](https://user-images.githubusercontent.com/46548557/156786634-af09a4da-609b-41f0-9347-13391e4d4466.png)

nebo pomocí příkazu: 

```bash
$ git clone https://github.com/BSPIKD/interactions.py-bot-template.git
```

### Instalace pm-core

Pro správné fungování je potřeba mít nainstalovaný podpůrný projekt [pm-core]() v src/pm-core.

**Instalace pm-core**
```bash
$ cd /path/to/project/src # $ cd /home/username/repos/pm-sandbox/src

# Nejnovější stabilní verze: "master", 
$ git clone 
# Nejnovější nestabilní verze: "unstable", 
# Konkrétní verze: "v1.0rc", 
```


**Instalace knihoven**

```bash
$ pip install -r requirements.txt
```

- do souboru [.env.template](.env.template) přidej [token](https://discord.com/developers/applications) svého bota a
  nastav spojení do databáze
    - následně soubor přejmenuj z `.env.template` na `.env`
- spouštěcí soubor: [`bot.py`](bot.py)

## Ostatní
- Seznam eventů [zde](https://discord.com/developers/docs/topics/gateway)
