from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Tuple

ADEQUACY_DIMENSIONS = ["A", "B", "C", "D"]
POTENTIAL_DIMENSIONS = ["E", "F", "G", "H", "I"]
ALL_DIMENSIONS = ADEQUACY_DIMENSIONS + POTENTIAL_DIMENSIONS

MANAGEMENT_LEVELS = ["B-1", "B-2", "B-3", "Ostalo"]


@dataclass(frozen=True)
class DimensionDetail:
    group: str
    name: str
    scale: Dict[int, str]
    description: Dict[int, str]


DIMENSION_DETAILS: Dict[str, DimensionDetail] = {
    "A": DimensionDetail(
        group="Adekvatnost",
        name="Svrhovito i sustavno razmišljanje",
        scale={
            1: "Disfunkcionalno, reaktivno ponašanje",
            2: "Ispod očekivanog razumijevanja",
            3: "Operativno adekvatno funkcioniranje",
            4: "Adaptivno vodstvo",
            5: "Sistemski arhitekt, mislilac",
        },
        description={
            1: "Fokusiran samo na razmatranje unutar svog tima. Ne uviđa širi kontekst, reaktivan. Gubi se u detaljima. Ne postavlja prioritete. Ignorira dugoročne posljedice.",
            2: "Traži razumijevanje, ali mu povezuje druge. Povremeno vidi uzroke, ali ne sustavno. Reagira na pritiske umjesto da planira. Misli linearno.",
            3: "Funkcionalno razumije širi poslovni kontekst, ali ne vidi vezu sa svojim područjem. Planira kvartalno, rijetko godišnje. Prati procese, ali ih ne preispituje. Donosi stabilne, ali ne inovativne odluke.",
            4: "Integrirano promišljanje sustava i odnosa. Vidi međuovisnosti. Povezuje kratkoročno, srednjoročno i dugoročno. Prepoznaje uzroke problema, ne samo simptome. Donosi odluke u širem kontekstu.",
            5: "Vidi organizaciju kao živ sustav. Predviđa posljedice odluka kroz funkcije. Integrira kratkoročno i dugoročno. Uči druge kako misliti sistemski.",
        },
    ),
    "B": DimensionDetail(
        group="Adekvatnost",
        name="Način vođenja i suradnje",
        scale={
            1: "Autoritativan i zatvoren",
            2: "Korektan, ali nesiguran",
            3: "Kooperativan, ali centraliziran",
            4: "Razvijajući vođa",
            5: "Servant lider",
        },
        description={
            1: "Koristi moć i strah. Ne sluša, prekida druge. Upravlja mikro. Stvara atmosferu nelagode.",
            2: "Sluša formalno, ali brani poziciju. Povremeno delegira, ali ne vjeruje timu. Izbjegava konflikte. Ovisi o odobravanju nadređenih.",
            3: "Timski rad uz ograničenu autonomiju. Očekuje inicijativu, ali je ne nagrađuje. Povremeno razvija druge. Konflikte rješava kompromisom.",
            4: "Jasno komunicira svrhu i očekivanja. Daje povjerenje i odgovornost. Potiče dijalog i konstruktivnu raspravu. Aktivno razvija suradnju među odjelima.",
            5: "Inspirira, ne upravlja kontrolom. Služi timu, ne egu. Kultura povjerenja i uzajamnog učenja.",
        },
    ),
    "C": DimensionDetail(
        group="Adekvatnost",
        name="Donošenje odluka i učenje",
        scale={
            1: "Impulzivno ili oklijevajuće",
            2: "Reaktivan pristup",
            3: "Racionalan, ali spor",
            4: "Iterativno donositelj odluka",
            5: "Učeći lider (safe-to-fail)",
        },
        description={
            1: "Odluke su ili ishitrene ili nercijepljene. Ignorira podatke. Krivi druge za greške. Ne preispituje odluke.",
            2: "Donosi odluke pod pritiskom, propušta prilike. Uči samo kad mora. Traži sigurne, poznate odluke. Slabo reflektira rezultate.",
            3: "Koristi podatke, ali bez eksperimentiranja. Analizira rizike, ne koristi ih za učenje. Revno dokumentira, ne prilagođava.",
            4: "Testira hipoteze, mjeri rezultate. Otvoreno priznaje greške. Donosi odluke uz konzultacije.",
            5: "Radi kroz male eksperimente (safe-to-fail). Koristi feedback za brzu prilagodbu. Aktivno traži različita mišljenja. Građanin učenja - širi lekcije.",
        },
    ),
    "D": DimensionDetail(
        group="Adekvatnost",
        name="Integritet i svrhovitost",
        scale={
            1: "Ego i korist",
            2: "Formalno etičan",
            3: "Integritet u korelaciji",
            4: "Moralni autoritet",
            5: "Moralni autoritet",
        },
        description={
            1: "Manipulira informacijama. Promovira osobni interes. Prepoznaje greške. Stvara strah od istine.",
            2: "Prati pravila, ali bez uvjerenja. Brani status quo. Izbjegava neugodne istine. Nedosljedan u ponašanju.",
            3: "Slijedi dogovoren kodeks. Poštuje procedure. Priznaje i ispravlja. Donosi konzistentne standarde. Drži riječ, ali bez šire svrhe.",
            4: "Dosljedno donosi teške odluke etično. Komunicira transparentno. Potiče otvorenost prema istini. Dosljedan u vrijednostima.",
            5: "Govori istinu i kad je neugodna. Usmjerava organizaciju prema svrsi. Utjelovljuje vrijednosti i integritet.",
        },
    ),
    "E": DimensionDetail(
        group="Potencijal",
        name="Samorefleksija",
        scale={
            1: "Bez uvida",
            2: "Selektivna refleksija",
            3: "Osnovna svjesnost",
            4: "Aktivna samorefleksija",
            5: "Metarefleksija",
        },
        description={
            1: "Ne vidi vlastitu ulogu. Odbija feedback. Krivi sustav ili druge. Ne uči iz iskustva.",
            2: "Prima feedback, ali ga racionalizira. Uočava pogreške naknadno. Samokritičan, ali bez promjene. Niska emocionalna svjesnost.",
            3: "Svjestan utjecaja na druge. Povremeno traži feedback. Priznaje vlastite greške. Mijenja ponašanja u poznatim situacijama.",
            4: "Traži povratnu informaciju unaprijed. Prakticira “kako sam pridonio” problemu. Uči iz više perspektiva. Svjesno nesvjesne uzorke.",
            5: "Otvoreno dijeli osobne lekcije. Potiče druge na refleksiju. Razumije unutarnje “ja”. Pokazuje ranjivost bez gubitka autoriteta.",
        },
    ),
    "F": DimensionDetail(
        group="Potencijal",
        name="Tolerancija paradoksa",
        scale={
            1: "Crno-bijelo razmišljanje",
            2: "Napetost između krajnosti",
            3: "Balans kroz pokušaje",
            4: "Svjestan polariteta",
            5: "Integrira suprotnosti",
        },
        description={
            1: "Traži jedno “točno” rješenje. Ne tolerira nejasnoće. Isključiv u rješenjima. Uporan u jednoj perspektivi.",
            2: "Osjeća frustraciju u nejasnoći. Brzo zauzima strane. Čeka da se “sve razjasni”. U stresu gubi širinu.",
            3: "Prepoznaje da su oba pola važna. Traži ravnotežu, ali intuitivno. Ne odustaje kad je dvosmisleno. Prihvaća različitost mišljenja.",
            4: "Koristi tenzije za inovaciju. Osjeća kada da djeluje ispod površine. Uspješno moderira suprotnosti. Djeluje mirno u nejasnoći.",
            5: "Dizajnira rješenja “i-i” umjesto “ili-ili”. Koristi paradokse za rast tima. Pomiruje brzinu i kvalitetu. Stvara sintezu iz konflikta.",
        },
    ),
    "G": DimensionDetail(
        group="Potencijal",
        name="Integrativno razmišljanje",
        scale={
            1: "U silosu",
            2: "Površna povezanost",
            3: "Osnovna integracija",
            4: "Transverzalni mislilac",
            5: "Holistički lider",
        },
        description={
            1: "Vidi samo svoje područje. Ograničen utjecaj na druge. Odbija suradnju. Brani “naš način”.",
            2: "Povezuje kako drugi doprinose. Prebacuje odgovornost. Slabo prevodi između timova.",
            3: "Zna pozvati ključne funkcije. Uključuje druge u planiranje. Prihvaća međuovisnosti. Surađuje konstruktivno.",
            4: "Razumije utjecaj svoje uloge. Gradi mostove između biznisa i tehnologije. Premošćuje međufunkcijske barijere. Graditelj mostova.",
            5: "Povezuje domene i discipline. Stvara multidisciplinarne timove. Holistički vidi ekosustav (unutarnje i vanjske). Vidi šire od organizacije.",
        },
    ),
    "H": DimensionDetail(
        group="Potencijal",
        name="Učenje iz povratne sprege",
        scale={
            1: "Odbacuje feedback",
            2: "Površno učenje",
            3: "Primijenjeno naučeno",
            4: "Sustavno učenje",
            5: "Katalizator učenja",
        },
        description={
            1: "Poriče, brani se, krivi druge. Ponavlja iste greške. Izbjegava retrospektive. Izolira tim od učenja.",
            2: "Uči samo u krizi. Pretvara feedback u formalnost. Slabo dokumentira lekcije.",
            3: "Redovito provjerava rezultate. Potiče dijeljenje u timu. Uvodi male promjene. Traži savjet kad ne zna.",
            4: "Integrira “learning loopove” u procese. Uči sustavno. Otvoreno priznaje greške. Transparentno dijeli pogreške. Mjeri učinak učenja.",
            5: "Ugrađuje učenje u strategiju. Traži negativne povratne informacije. Nagrađuje druge za otvorenost. Gradi učeću kulturu.",
        },
    ),
    "I": DimensionDetail(
        group="Potencijal",
        name="Etika i povjerenje",
        scale={
            1: "Nepouzdan i proračunat",
            2: "Oportunistički etičan",
            3: "Uglavnom etičan",
            4: "Transparentni i pošteni",
            5: "Moralni kompas organizacije",
        },
        description={
            1: "Manipulira, skriva informacije. Zloupotrebljava formalnosti. Krši dogovore. Gubi povjerenje okoline.",
            2: "Poštuje etiku dok mu koristi. Selektivno dijeli informacije. Nedosljedan prema različitima. U tišini prelazi preko problema.",
            3: "Postupa korektno u većini situacija. Drži obećanja. Poštuje povjerenje. Pokazuje osnovno povjerenje.",
            4: "Transparentan i pravedan, ali s granicama. Aktivno brani vrijednosti tima. Otvoren kad griješi. Stvara povjerenje i pod pritiskom.",
            5: "Inspirira povjerenje kroz djela. Model etike i integriteta. Donosi odluke vođen vrijednostima. Stvara etičku kulturu.",
        },
    ),
}


CATEGORY_RULES: List[Tuple[str, float, float]] = [
    ("Primjer", 4.0, 4.0),
    ("Potencijal", 3.0, 4.0),
    ("Adekvatan", 3.0, 2.5),
    ("Neadekvatan s potencijalom", 2.5, 3.0),
]


def calculate_scores(dimensions: Dict[str, int]) -> Dict[str, float | str]:
    adequacy = sum(dimensions[d] for d in ADEQUACY_DIMENSIONS) / len(ADEQUACY_DIMENSIONS)
    potential = sum(dimensions[d] for d in POTENTIAL_DIMENSIONS) / len(POTENTIAL_DIMENSIONS)
    category = "Eliminirati"
    for name, min_adequacy, min_potential in CATEGORY_RULES:
        if adequacy >= min_adequacy and potential >= min_potential:
            category = name
            break
    return {
        "adequacy": round(adequacy, 2),
        "potential": round(potential, 2),
        "category": category,
    }


def summarize_by_category(assessments: List[Dict]) -> List[Dict]:
    total = len(assessments)
    counts: Dict[str, int] = {}
    for assessment in assessments:
        category = assessment.get("category", "Eliminirati")
        counts[category] = counts.get(category, 0) + 1
    summary = []
    for category, count in sorted(counts.items(), key=lambda item: item[0]):
        percentage = (count / total * 100) if total else 0.0
        summary.append({
            "category": category,
            "count": count,
            "percentage": round(percentage, 2),
        })
    return summary
