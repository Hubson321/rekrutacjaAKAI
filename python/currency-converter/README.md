# Currency converter

1. Mechanizm został uodporniony na nie występowanie pliku ```ratios.json```, w takim przypadku twory się plik z obecnie wymaganym kursem.
2. W przypadku gdy plik ```ratios.json``` istnieje, ale jest pusty, obecnie wymagany kurs jest zapisywany do pliku.
3. Gdy kurs istnieje w pliku, ale nie jest aktualny zappisywany jest poprawny kurs z dobrą datą.
4. Gdy kurs istnieje i jest aktualny, pobierana jest wartość z pliku, bez konieczności łącenia się z API. 