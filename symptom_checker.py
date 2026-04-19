"""
Symptom Checker Chatbot
=======================
A simple AI-powered chatbot that uses keyword-based analysis and rule logic
to assess reported symptoms and suggest whether to seek medical attention.

Demonstrates: classes, dictionaries, loops, conditionals, string processing.
Author: Hanne Emaus
"""

SYMPTOMS_DB = {
    "brystsmerter": {"alvorlighet": 3, "kategori": "hjerte", "råd": "Kontakt lege umiddelbart eller ring 113."},
    "kortpustethet": {"alvorlighet": 3, "kategori": "luftveier", "råd": "Søk legehjelp raskt, særlig ved hvile."},
    "feber": {"alvorlighet": 2, "kategori": "infeksjon", "råd": "Hvil, drikk mye og mål temperaturen. Over 39°C → lege."},
    "hodepine": {"alvorlighet": 1, "kategori": "nevro", "råd": "Prøv paracetamol og hvile. Vedvarer → lege."},
    "kvalme": {"alvorlighet": 1, "kategori": "mage", "råd": "Lett kost og rikelig væske. Vedvarer over 2 dager → lege."},
    "svimmelhet": {"alvorlighet": 2, "kategori": "nevro", "råd": "Sitt/legg deg ned. Vedvarer eller er kraftig → lege."},
    "utslett": {"alvorlighet": 2, "kategori": "hud", "råd": "Unngå å klø. Sprer seg raskt eller gir pusteproblemer → øyeblikkelig hjelp."},
    "magesmerter": {"alvorlighet": 2, "kategori": "mage", "råd": "Kraftige smerter eller vedvarer over 6 timer → lege."},
    "tretthet": {"alvorlighet": 1, "kategori": "generell", "råd": "Hvil og drikk nok. Ekstrem tretthet uten årsak → lege."},
    "hoste": {"alvorlighet": 1, "kategori": "luftveier", "råd": "Blodhoste eller vedvarer over 3 uker → lege."},
}

ALVORLIGHET_TEKST = {
    1: "Lav – kan vanligvis håndteres hjemme",
    2: "Moderat – observer nøye, kontakt lege ved forverring",
    3: "Høy – søk hjelp raskt",
}


class SymptomChecker:
    def __init__(self):
        self.registrerte_symptomer = []
        self.maks_alvorlighet = 0

    def analyser_input(self, tekst: str) -> list[str]:
        tekst_lower = tekst.lower()
        funnet = []
        for symptom in SYMPTOMS_DB:
            if symptom in tekst_lower:
                funnet.append(symptom)
        return funnet

    def legg_til_symptomer(self, nye: list[str]):
        for s in nye:
            if s not in self.registrerte_symptomer:
                self.registrerte_symptomer.append(s)
                alv = SYMPTOMS_DB[s]["alvorlighet"]
                if alv > self.maks_alvorlighet:
                    self.maks_alvorlighet = alv

    def generer_svar(self, symptomer: list[str]) -> str:
        if not symptomer:
            return (
                "Jeg fant ingen kjente symptomer i det du skrev. "
                "Prøv å beskrive det du kjenner, f.eks. 'feber', 'hodepine' eller 'magesmerter'."
            )

        linjer = ["Jeg registrerte følgende symptomer:\n"]
        for s in symptomer:
            info = SYMPTOMS_DB[s]
            alv_stjerner = "●" * info["alvorlighet"] + "○" * (3 - info["alvorlighet"])
            linjer.append(f"  {s.capitalize()} [{alv_stjerner}]")
            linjer.append(f"  → {info['råd']}\n")

        if self.maks_alvorlighet == 3:
            linjer.append("ADVARSEL: Ett eller flere symptomer krever rask medisinsk vurdering.")
        elif self.maks_alvorlighet == 2:
            linjer.append("Observer symptomene nøye. Kontakt lege hvis de forverres.")
        else:
            linjer.append("Symptomene kan sannsynligvis håndteres hjemme. Kontakt lege ved forverring.")

        linjer.append(
            f"\nSamlet alvorlighetsgrad: {ALVORLIGHET_TEKST[self.maks_alvorlighet]}"
        )
        return "\n".join(linjer)

    def oppsummering(self) -> str:
        if not self.registrerte_symptomer:
            return "Ingen symptomer registrert i denne samtalen."
        alle = ", ".join(self.registrerte_symptomer)
        return f"Symptomer i denne samtalen: {alle}\nAlvorlighetsgrad: {ALVORLIGHET_TEKST[self.maks_alvorlighet]}"


def main():
    print("=" * 55)
    print("  Symptom-sjekker  |  Skrevet av Hanne Emaus")
    print("  Kombinerer helsekunnskap med Python og AI-logikk")
    print("=" * 55)
    print("\nHei! Beskriv symptomene dine på norsk.")
    print("Skriv 'avslutt' for å avslutte, 'oppsummering' for sammendrag.\n")
    print("MERK: Dette er et læringsprosjekt, ikke medisinsk rådgivning.\n")

    checker = SymptomChecker()

    while True:
        bruker_input = input("Du: ").strip()

        if not bruker_input:
            continue
        if bruker_input.lower() == "avslutt":
            print("\n" + checker.oppsummering())
            print("\nTa vare på deg selv! Ha en god dag.")
            break
        if bruker_input.lower() == "oppsummering":
            print("\n" + checker.oppsummering() + "\n")
            continue

        symptomer = checker.analyser_input(bruker_input)
        checker.legg_til_symptomer(symptomer)
        svar = checker.generer_svar(symptomer)
        print(f"\nBot: {svar}\n")


if __name__ == "__main__":
    main()
