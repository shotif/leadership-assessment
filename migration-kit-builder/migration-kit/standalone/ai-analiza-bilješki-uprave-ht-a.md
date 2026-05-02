# AI analiza bilješki Uprave HT-a
- **Conversation ID:** `750d6651-d9b9-4666-9fa2-eee25ca73c13`
- **Created:** 2026-03-14T20:33:29.656588+00:00
- **Updated:** 2026-03-14T20:46:12.734357+00:00
- **Messages:** 8

---

## Human  *(2026-03-14T20:33:30.082761+00:00)*

analiziraj ove rukom pisane bilješke o radu Uprave HT-a i kako im AI može pomoći

## Assistant  *(2026-03-14T20:34:54.361614+00:00)*

Let me look at the uploaded PDF to analyze the handwritten notes.

The PDF is a binary file with an embedded image. The document context shown in the prompt shows the first page but it appears empty in the document content. Let me try to use bash to extract the image from the PDF to see what it contains.

Actually, looking at the document tag in the prompt, it says `<document_content page="1"></document_content>` which is empty. The PDF likely contains a scanned image. Let me try to extract and view it.

No network access. Let me try using existing tools to extract the image from the PDF.

Now I can see the handwritten notes. Let me transcribe and analyze them.

The notes appear to be about the "Uprava" (Board/Management) of HT and how AI can help. Let me transcribe:

**Title/Header:** "Uprava - Efikasne i fokusirane rasprave uz kraće vrijeme pripreme"
(Board - Efficient and focused discussions with shorter preparation time)

**Left column - formalni (formal):**
- odluke - Irena
- produženje ugovora
- razlaženje oko projekta
- uvjeta

**Right column - neformalni (informal):**

- teme
- materijali u petak →
- prezentacije → struktura
- što se traži?
- zaključak

**Below left:** Arhiva Uprave → pristup? → Irena

**Below right:** zapisnik + APs (Action Points)
- "Goni tko prezentira"

**Second section:**
"Ara Neigor - zapisnik, bilješke, APs → AI za to!
na početku se prolazi AP listu"

**Third section:**
"AI za pripremu iz materijala - relevantnosti?
→ prolaze po temama, područja, za" — it looks like the notes are exploring how AI could help with preparing materials by filtering for relevance and organizing them by topic and area.

**Fourth section:**
"AI čita AP-ove, priprema ih za početak sjednice"

**Fifth section:**
"priprema inputa za prezente - što želimo znati
prikupljanje feedbacka
→ Northstar     AI kao 8., 9., 10. član Uprave
                - devil's advocate"

The core idea emerging here is using AI to streamline board preparation and discussions — handling action points, cross-checking policies against company archives with deeper analysis, and ultimately positioning AI as an additional participant that challenges assumptions and plays devil's advocate during meetings. I'm also seeing how AI could pull from the company archive using RAG, reading through action points to prepare them before meetings start, and helping prepare presentation inputs while gathering feedback. There's also this interesting idea of AI acting as additional board members—a devil's advocate role to challenge decisions and push deeper analysis.Odlično, bilješke su čitljive. Evo kompletne analize.

---

## 📋 Transkript bilješki

**Naslov:** *Uprava — Efikasne i fokusirane rasprave uz kraće vrijeme pripreme*

**Formalni sastanci** | **Neformalni sastanci**
--- | ---
Odluke – Irena | Teme
Produženje ugovora | Materijali u petak →
Razlaganje oko projekta/uvjeta | Prezentacije → struktura, što se traži?, zaključak
Arhiva Uprave → pristup? → Irena | Zapisnik + APs — *"Goni tko prezentira"*

---

## 🤖 Identificirani AI use caseovi (iz bilješki)

### 1. AI za zapisnik, bilješke i Action Points
> *"Ara Neigor — zapisnik, bilješke, APs → **AI za to!** Na početku se prolazi AP listu"*

AI automatski generira zapisnik sa sjednice, ekstrahira akcijske točke i na sljedećoj sjednici priprema pregled statusa prethodnih APs. Ovo je najzreliji, najlakše implementabilni use case — može krenuti odmah.

---

### 2. AI za pripremu materijala — relevantnost i dubinska razrada
> *"AI za pripremu iz materijala — relevantnosti? → prolaze po temama, područjima, za Krezu, Sirišu, etc. X-check politike (Pluto) → dublja razrada, pitanja, RAG iz kompanijske arhive"*

Ovdje se vidi konkretan RAG scenarij: AI čita materijale koji dolaze uoči sjednice, provjerava ih u odnosu na internu politiku/arhivu (Pluto?), i za svakog člana Uprave priprema personalizirani brief — što je relevantno za njihov resor, koje su ključne odluke, koja pitanja treba postaviti.

---

### 3. AI čita AP-ove i priprema otvaranje sjednice
> *"AI čita AP-ove, priprema ih za početak sjednice"*

Strukturirani opening za svaku sjednicu: AI generira kratki status update svih otvorenih akcijskih točaka s prethodnih sjednica — tko je zadužen, što je zatvoreno, što kasni. Predsjedniku Uprave dolazi gotov uvod, bez manualne pripreme.

---

### 4. AI za pripremu inputa za prezentere + prikupljanje feedbacka
> *"Priprema inputa za prezente — što želimo znati, prikupljanje feedbacka → Northstar"*

Prije nego prezenter dođe pred Upravu, AI na temelju agende i profila prezentacije generira: što Uprava želi znati, koja su "teška" pitanja, koje su potencijalne rupe u argumentaciji. Northstar kao referentni okvir za strateško pozicioniranje.

---

### 5. AI kao 8./9./10. član Uprave — Devil's Advocate
> *"AI kao 8., 9., 10. član Uprave — devil's advocate"*

Ovo je najambiciozniji koncept — i najzanimljiviji. AI ne samo asistira već aktivno participira: analizira prijedloge pred Upravu, donosi alternativne perspektive, izaziva pretpostavke, identificira rizike koje nitko nije izgovorio. Analogija s "devil's advocate" je precizna — AI ima slobodu reći ono što nitko od prisutnih ne želi/smije.

---

## 🔑 Ključna observacija

Bilješke pokazuju zrelo razmišljanje — nije "AI generalno pomaže", već su identificirani **konkretni workflow trenuci** u radu Uprave gdje AI može reducirati pripremu i povećati kvalitetu rasprave. Logičan redoslijed implementacije:

1. **Odmah:** Zapisnik + APs (gotove tehnologije, jasna vrijednost)
2. **Q2:** Personalizirani brief iz materijala (RAG nad arhivom)
3. **Q3/Q4:** Devil's advocate uloga (zahtijeva kontekst i povjerenje)

Treba li od ovoga napraviti formalni use case slide ili brief za Upravu?

## Human  *(2026-03-14T20:37:05.493892+00:00)*

trebam pomoć da razradimo ove use caseve, što je low hanging fruit, što je mid što long term, koji pristup u daljnoj definiciji trebamo primijeniti, koje alate možemo testirati, koji su kriteriji uspješnosti i kako ćemo ih mjeriti?

## Assistant  *(2026-03-14T20:37:20.170723+00:00)*

Robi wants to develop these use cases into a structured roadmap. Let me think about this properly before asking clarifying questions - I should provide real substance but also understand the context better.

Actually, let me ask a few targeted questions first to make this maximally useful, since the answer will vary significantly based on:
1. Existing tech stack / what's already available at HT
2. Who owns this - is this for Uprava directly or for a broader team?
3. What's the deployment environment constraint

Let me ask focused questions.Prije nego zaronimo, trebam razumjeti par ključnih stvari da razrada bude konkretna, a ne generična.

Let me wait for the user's response.

## Human  *(2026-03-14T20:38:04.806051+00:00)*

Q: Koji je krajnji cilj ove razrade?
A: Interna pilot implementacija za Upravu

Q: Što je trenutno dostupno u HT-u (tech)?
A: Microsoft 365 / Copilot licenca, Interna dokumentacijska baza (SharePoint/intranet), ChatGPT Enterprise, Gemini Enterprise, NotebookLM Enterprise

Q: Tko je vlasnik ovih use caseva i tko ih testira?
A: Robi osobno / mali tim

## Assistant  *(2026-03-14T20:39:17.037896+00:00)*

Great context. Now I can give a concrete, actionable breakdown. Let me structure this properly:

- 5 use cases from the notes
- Low/mid/long term horizon
- Approach for further definition
- Tools to test (from available: M365/Copilot, SharePoint, ChatGPT Enterprise, Gemini Enterprise, NotebookLM Enterprise)
- Success criteria and measurement

Let me think through each use case:

1. **Zapisnik + APs** - LOW HANGING FRUIT
   - Tools: Copilot in Teams (transcription + summary), or ChatGPT Enterprise
   - Easy to test, clear value, low risk
   
2. **AI čita AP-ove, priprema otvaranje sjednice** - LOW/MID
   - Structured AP tracking is manageable here
   - Copilot + SharePoint or ChatGPT Enterprise with document input would work well

3. **Personalizirani brief iz materijala (RAG)** - MID TERM
   - This requires RAG setup over the archive, which NotebookLM Enterprise handles perfectly
   - More complex setup but solid long-term value

4. **Priprema inputa za prezentere + feedback** - MID TERM
   - Still need to define the workflow here

, but ChatGPT Enterprise or Gemini Enterprise can handle the execution

5. **Devil's Advocate / 8.-10. član Uprave** - LONG TERM
   - This is the most demanding piece—needs institutional trust and likely a custom GPT or fine-tuned model to really workSavršen setup — imate sve što treba da krenete bez ijednog IT ticketa. Evo kompletne razrade.

---

## 🗺️ Use Case Roadmap: AI za Upravu HT

---

### 🟢 LOW HANGING FRUIT — pilotiraj u 4 tjedna

---

#### UC1 · Zapisnik + Action Points
**Problem:** Zapisnik se piše manualno, APs se gube između sjednica, nitko ne prati status.

**Pristup definicije:**
Definiraj output format koji Uprava prihvaća — što je zapisnik, što su APs, tko je vlasnik, koji je rok. Tek onda alat.

**Alati za test:**
- **Copilot u Teams** → automatska transkripcija + summary ako je sjednica online/hybrid
- **ChatGPT Enterprise** → ako je sjednica fizička: snima se audio (telefon), transkript se paste-a, Copilot/ChatGPT generira zapisnik prema definiranom promptu
- **SharePoint** → pohrana strukturiranih APs s owner/deadline kolonama

**Kriteriji uspješnosti:**
| Metrika | Baseline | Target |
|---|---|---|
| Vrijeme pisanja zapisnika | ~2-3h | <30 min |
| % APs s definiranim vlasnikom | mjeri se u prvom tjednu | 100% |
| % APs zatvorenih do sljedeće sjednice | mjeri se u prvom tjednu | +20pp vs. baseline |

**Kako mjeriti:** Uzmi 3 prethodna zapisnika kao baseline, usporedi s prvim 3 AI-generiranim.

---

#### UC2 · AP pregled na otvaranju sjednice
**Problem:** Svaka sjednica kreće od nule — nitko ne zna što je zatvoreno, što kasni.

**Pristup definicije:**
Treba ti samo strukturiran AP log (Excel/SharePoint lista). AI tada generira opening brief format: "Zatvoreno X, otvoreno Y, kasni Z — vlasnik je..."

**Alati za test:**
- **ChatGPT Enterprise** → paste AP lista + prompt "pripremi opening za sjednicu"
- **Copilot u Excel/SharePoint** → ako je AP log tamo, direktno summary

**Kriteriji uspješnosti:**
| Metrika | Target |
|---|---|
| Priprema openinga | <5 min vs. 20+ min manualno |
| Pokrivenost svih APs u openingu | 100% |
| Subjektivna ocjena članova Uprave (1-5) | ≥4 |

---

### 🟡 MID TERM — pilotiraj u 2-3 mjeseca

---

#### UC3 · Personalizirani brief iz materijala (RAG nad arhivom)
**Problem:** Materijali dolaze u petak, svaki ih čita sam, bez konteksta iz prethodnih odluka i politika.

**Pristup definicije:**
Ovo je najkompleksniji setup u ovoj grupi. Potrebno je:
1. Definirati koji dokumenti čine "arhivu" (odluke Uprave, politike, strateški planovi)
2. Organizirati ih u NotebookLM ili SharePoint s Copilotom
3. Definirati persona per član Uprave — što je relevantno za Financije vs. Tehničku vs. Komercijalu

**Alati za test:**
- **NotebookLM Enterprise** → idealan za ovo; uploadaš sve materijale za sjednicu + relevantne politike, dobiješ strukturirani Q&A i brief. Nema potrebe za custom RAG developmentom.
- **Gemini Enterprise** → alternativa s boljim document grounding-om za veće arhive

**Workflow koji testiraš:**
```
Materijali dolaze u četvrtak → upload u NotebookLM notebook za tu sjednicu 
→ AI generira brief po temama → svaki član dobiva svoj "pogled" 
→ petak popodne: 15 min čitanja umjesto 2h
```

**Kriteriji uspješnosti:**
| Metrika | Target |
|---|---|
| Subjektivna pripremljenost članova (1-5) | ≥4 |
| Broj pitanja na sjednici koja su "očekivana" | -30% (manje iznenađenja) |
| Vrijeme pripreme per materijal | <20 min vs. 60+ min |

---

#### UC4 · Priprema pitanja i feedbacka za prezentere
**Problem:** Prezenter dolazi, rasprava je reaktivna, nema strukturiranog feedbacka.

**Pristup definicije:**
Definiraj što Uprava želi znati od svakog tipa prezentacije (investicija, projekt, regulativa, HR...). To postaje **prompt template** koji AI primjenjuje na svaki deck koji dolazi.

**Alati za test:**
- **ChatGPT Enterprise** → prezentacija se uploaduje kao PDF, AI generira: "3 ključna pitanja", "potencijalni rizici koji nisu adresirani", "strateška usklađenost s X"
- **Copilot u PowerPoint** → za brzu analizu strukture decka

**Northstar konekcija iz bilješki:** Ovdje se Northstar okvir može koristiti kao evaluacijski kriterij koji AI uvijek primjenjuje.

**Kriteriji uspješnosti:**
| Metrika | Target |
|---|---|
| Kvaliteta pitanja na sjednici (subjektivno, 1-5) | ≥4 |
| Broj "nenagovorenih rizika" koje AI identificira | mjeri se kao discovery metrika |
| Prezenterovo zadovoljstvo jasnoćom expectations (1-5) | ≥4 |

---

### 🔴 LONG TERM — definiraj u Q3, pilotiraj u Q4

---

#### UC5 · AI kao Devil's Advocate (8./9./10. član Uprave)
**Problem:** Groupthink, nedostatak strukturiranog izazivanja pretpostavki, nitko ne želi biti "onaj koji pita glupo pitanje".

**Zašto long term:**
Ovo nije tehnički problem — ovo je problem **institucionalnog povjerenja**. Uprava mora prvo vidjeti AI kao korisnog asistenta (UC1-4) da bi ga prihvatila kao "adversarialnog savjetnika". Preuranjeno uvođenje ovog modela može politički potopiti cijeli program.

**Pristup definicije (kad dođe vrijeme):**
- Custom GPT u ChatGPT Enterprise s "karakterom" koji ima kontekst HT-a, strategije, regulatornog okvira, i eksplicitnu ulogu: "Tvoj jedini zadatak je pronaći što je krivo u ovom prijedlogu."
- Testirati prvo s Robijem i jednim/dva člana Uprave koji su open za to — ne na plenarnoj sjednici

**Kriteriji uspješnosti (za definiciju pilota):**
- Broj identificiranih rizika koji su prošli u implementaciju (retrospektivno)
- Udio odluka gdje je AI challenge promijenio finalni prijedlog
- Povjerenje i prihvaćenost alata (intervju s Upravom nakon 3 sjednice)

---

## 🧭 Pristup u daljnjoj definiciji (za sve UC-ove)

Za svaki use case slijedi isti mini-framework prije nego kreneš u alat:

```
1. PROBLEM STATEMENT       → Koji je točno pain, tko ga osjeća, koliko često?
2. OUTPUT DEFINICIJA       → Kako izgleda "dobar" output? Koji je format, tko čita?
3. INPUT MAPPING           → Koji dokumenti/podaci trebaju ući u AI?
4. PROMPT DESIGN           → Koji je sistemski prompt? Testirati 3-5 varijanti.
5. PILOT DESIGN            → 2-3 sjednice, isti tim, mjeriš baseline vs. AI.
6. FEEDBACK LOOP           → Kratki feedback nakon svake sjednice (3 pitanja, max).
```

---

## 🛠️ Tool matrix po use caseu

| Use Case | Primarni alat | Alternativa | Napomena |
|---|---|---|---|
| UC1 Zapisnik/APs | Copilot (Teams) | ChatGPT Enterprise | Copilot ako sjednice u Teamsu |
| UC2 AP opening | ChatGPT Enterprise | Copilot (Excel) | Najjednostavniji start |
| UC3 Brief iz arhive | **NotebookLM Enterprise** | Gemini Enterprise | NotebookLM je made for this |
| UC4 Pitanja za prezentere | ChatGPT Enterprise | Copilot (PowerPoint) | Custom GPT template |
| UC5 Devil's Advocate | Custom GPT (ChatGPT Ent.) | — | Tek u Q4 |

---

## 🚀 Preporuka: gdje početi sutra

**Tjedan 1:** UC2 — pripremi AP log iz jednog prethodnog zapisnika, paste u ChatGPT, napiši prompt koji generira opening brief. Pokaži jednom članu Uprave. Brz win, nula infrastrukture.

**Tjedan 2-3:** UC1 — definiraj template za zapisnik + APs, testiraj na sljedećoj sjednici.

**Tjedan 4:** UC3 — otvori NotebookLM Enterprise notebook za jednu nadolazeću temu, uploadaj materijale + relevantne politike, daj jednom članu Uprave na probu.

---

Hoćeš da krenemo odmah na jedan od ovih — npr. napišemo prompt template za UC2 ili UC1 koji možeš testirati na sljedećoj sjednici?

## Human  *(2026-03-14T20:41:21.576004+00:00)*

Sjednice Uprave su u pravilu uživo u boardroomu, teoretski se mogu snimati preko Teamsa, ali mi se postavlja pitanje kako će AI prepoznati govornike i znati tko je što rekao? Može li tajnica Uprave asistirati AI-u u tome? Uzmi to u obzir pa redefiniraj cijeli prijedlog, treba mi jedinstveni dokument koji ću proći sa svojim AI timom da napravimo akcijski plan. Napiši prompt template za prva 2 UC

## Assistant  *(2026-03-14T20:46:12.715695+00:00)*

Robi wants a comprehensive document to share with his AI team, plus prompt templates for UC1 and UC2. The key new constraint is speaker identification in live boardroom meetings. Let me think through this carefully.

For speaker identification in boardroom recordings:
1. Teams can record and transcribe, but speaker identification requires that participants are logged into Teams on their devices
2. In a boardroom setting, people might not be on individual devices
3. The assistant (tajnica) could help by:
   - Manually noting who spoke when (time-stamped notes)
   - Using a structured "annotation" approach
   - Post-meeting: reviewing transcript and tagging speakers
   
I'm weighing several approaches here: tajnica could manually tag speakers in the transcript after the meeting, or if board members join individually from their devices, Teams would handle identification automatically. There are also specialized diarization tools available, though they typically require cloud uploads which raises privacy concerns. A hybrid approach combining Teams recording with tajnica's quick annotation pass seems most practical for this context. Now I should create a proper document to present these options and templates to the team.

Now I need to create a comprehensive Word document that covers:
1. The redefined use cases taking into account the boardroom/speaker identification challenge
2. The approach for the AI team to create an action plan
3. Prompt templates for UC1 (Minutes + APs) and UC2 (AP opening brief)

Key insight about speaker identification:
- Teams can transcribe but in boardroom, people aren't individually logged in
- Options:
  1. **Hybrid annotation**: Teams records audio/video, tajnica (secretary) annotates the transcript with speaker names post-meeting (she knows all the voices/faces)
  2. **Structured note-taking by tajnica**: During meeting, she takes structured notes with speaker attribution, then AI processes those notes
  3. **Teams Room device**: If HT boardroom has a Teams Room setup with individual microphone tracking
  4. **Manual tagging in transcript**: Tajnica reviews auto-transcript and does find-replace of "[Speaker 1]" → "[Ime Prezimena]"

The tajnica role is crucial—she becomes the "human in the loop" for speaker identification, which is actually a solid design pattern. Now I'm ready to build out the comprehensive document.Odlično pitanje — ovo je ključni gap koji treba razriješiti arhitekturalno, ne samo tehnički. Krećem pisati dokument.

Dokument je spreman — evo što sadrži i zašto su ključne odluke takve kakve su.

---

**Najvažnija stvar koju dokument razrađuje** je arhitekturalni odgovor na tvoje pitanje o speaker ID-u: tajnica nije "pomoćnica AI-u" — ona je **Speaker Identification layer** bez kojeg UC1 ne funkcionira. Dokument to tretira kao arhitekturalni preduvjet, ne kao nice-to-have, i predlaže konkretan predložak bilješki koji ona može odmah koristiti.

**Što dokument sadrži:**
- Puno poglavlje o Speaker ID problemu s dvije varijante (preporučena: strukturirane bilješke tajnice, bez snimanja)
- Predložak bilješki za tajnicu koji se može odmah koristiti
- UC1 i UC2 — kompletan pilot dizajn, kriteriji uspješnosti i prompt template koji možeš sutra testirati
- UC3–UC5 — arhitekturalni sažetak s preduvjetima (za razradu u idućem koraku)
- 6-koračni okvir koji AI tim primjenjuje za svaki budući UC
- 4-tjedni akcijski plan s vlasnicima

**Preporučeni sljedeći korak:** Sesija s tajnicom Uprave — ona je kritična točka sustava i vrijedi 30 minuta njenog vremena uložiti prije prve sjednice.
