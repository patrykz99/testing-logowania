# (PL) Automatyczne testowanie strony logowania SauceDemo (Python + POM, Selenium, Docker)

## 📝 Opis projektu

Projekt przedstawia przykładowe wdrożenie automatycznych testów funkcjonalnych procesu logowania na stronie [SauceDemo](https://www.saucedemo.com/) przy użyciu Selenium WebDriver oraz języka Python. Zastosowałem wzorzec projektowy **Page Object Model (POM)** (głównie w celu wcześniejszej nauki tego wzorca i chęci zastosowania w tym projekcie), testy jednostkowe (`unittest`) oraz konteneryzację środowiska uruchomieniowego przy pomocy **Dockera**.

## Co testuje projekt?

- Logowanie poprawnymi danymi.
- Walidacja błędnych danych (poprzez komunikaty o błędach).
- Walidacja pól formularza (wszystkie puste pola, pojedyńcze puste pole).

## Technologie i narzędzia

- **Python ver. 3.12**
- **Selenium WebDriver**
- **unittest**
- **Docker**

## Jak uruchomić projekt?

### Lokalnie:

```bash
pip install -r requirements.txt
```

```bash
python login_test.py
```

### Przy użyciu Dockera:

```bash
docker build -t testing-logowania .
```

```bash
docker run --rm testing-logowania
```


