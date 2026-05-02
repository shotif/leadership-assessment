# In-chat digest prompt — PetAIk

Paste **everything below the `---`** into a fresh Claude chat. Save Claude's markdown reply over the existing `migration-kit/projects/petaik/context-digest.md`.

If your Claude session has a context limit, paste the source-material section and the instructions in two messages.

---

You are synthesizing a context digest for a Claude Enterprise project being rebuilt from a previous account. The digest will be pasted into the first chat in the new project to prime its memory. Project name: **PetAIk** (slug `petaik`).

## Output format

Produce a Markdown document of roughly 600 words with these sections, in this order:

1. **Purpose** — what the project is for.
2. **Key decisions taken so far** — bullet list of concrete decisions with their rationale.
3. **Current state** — what's been produced, what's in flight.
4. **Important artifacts** — named deliverables / docs / datasets to remember.
5. **Open threads** — what's still undecided or unfinished.
6. **What to ask Claude next** — the most likely follow-up prompts when picking this project up.

Ground the digest in concrete signal from the source material. Use named entities (people, tools, programs). Drop hedging.

## Source material

### Custom instructions

_(none)_

### Knowledge files attached to this project

_(none)_

### Project memory (from `memories.json`)

_(none)_

### Conversation transcripts (2)

# PetAIk Razvoj koncepta sa Opusom
- **Conversation ID:** `9a056900-977e-4b71-adf2-273136c89a39`
- **Created:** 2026-04-02T20:03:54.664126+00:00
- **Updated:** 2026-04-02T20:44:17.796215+00:00
- **Messages:** 8

---

## Human  *(2026-04-02T20:03:54.986676+00:00)*

Razradio sam osnove koncepta sa Sonnetom, sada trebam tvoju pomoć. Pročitaj, analiziraj, postavi pitanja, pa razradi zajedno sa mnom:

## Assistant  *(2026-04-02T20:04:33.087373+00:00)*

Robi wants me to read the uploaded file, analyze it, and then discuss it with him. Let me first read the file.

This is a concept called "PetAIk" (a play on "petak" = Friday in Croatian, combined with AI) — essentially a structured AI upskilling/production day for HT employees. It was developed with Sonnet and now Robi wants me to analyze it, ask questions, and help develop it further.

Let me analyze the strengths and gaps of this concept, then ask targeted questions.Pročitao sam. Solidan konceptualni okvir — Sonnet je dobro strukturirao osnove. Filozofija "produkcijski dan budućnosti" je pravi framing za Board, i segmentacija po načinu rada umjesto hijerarhije je pametan potez.

Evo što mi odmah upada u oči kao snažno, i gdje vidim rupe ili rizike:

**Što drži vodu:**
Trostruka funkcija (upskilling + produktivnost + kultura) kroz jedan mehanizam je elegantan argument. Floating PetAIk za front rješava najčešći razlog zašto ovakve inicijative padnu — "ali mi ne možemo petkom". AI Champion kao peer, ne ekspert — to je kulturno točno za HT.

**Gdje vidim praznine ili napetosti:**

Prvo — **odnos prema DT grupi**. Ovo nigdje ne adresira kako se PetAIk pozicionira prema grupnim AI inicijativama (NeXT, grupni upskilling programi). Board će pitati "zašto naše vlastito, a ne grupno rješenje?" Trebaš odgovor.

Drugo — **mjerenje bez ROI-ja**. Dokument kaže "izbjegni ROI u ranoj fazi" i to je taktički ispravno, ali nedostaje konkretan prijedlog *što* mjerite umjesto toga. NPS zaposlenika je slab proxy sam za sebe.

Treće — **AI Champion kapacitet**. Tko su ti ljudi realno? Imaju li uopće slack u rasporedu za pripremu tjedan dana unaprijed? Ovo je točka gdje koncept može pasti u implementaciji.

Četvrto — **frekvencija**. Svaki petak je ambiciozno za pilot. Bi li "svaki drugi petak" bio realniji početak i lakši za Board approval?

Peto — **Show blok rizik**. 60 minuta showcasea s ljudima koji tek uče AI alate može biti neugodno iskustvo ako nije dobro facilitirano. "Nedovršeno je OK" je lijepa izjava, ali kultura HT-a to možda ne podržava u praksi.

Prije nego krenem u razradu, trebam tvoj input na par stvari:

Good, I've asked the key questions. Waiting for Robi's responses.

## Human  *(2026-04-02T20:04:57.367601+00:00)*

Q: Koji je primarni audience za prvi dokument koji radimo?
A: Board 1-pager / deck

Q: Koliko agresivno želiš ići s frekvencijom u pilotu?
A: 1x mjesečno za početak

Q: Kako se ovo pozicionira prema DT grupi?
A: HT-own inicijativa, neovisna

## Assistant  *(2026-04-02T20:05:20.829152+00:00)*

Robi wants:
1. Board 1-pager/deck as the first deliverable
2. 1x monthly frequency for pilot (more conservative than the original doc)
3. HT-own initiative, independent from DT group

This changes the framing significantly. Let me think through the implications before jumping into production.

Key shifts from the original concept:
- Monthly frequency means each PetAIk carries more weight — it's an "event" not a "routine" in the early phase
- Board deck needs to justify why HT is doing this independently, not through DT group programs
- The "every Friday" aspiration becomes the long-term vision, not the starting point

- Before I draft the Board material, I need to clarify a few critical things: why the independence from DT (is it a speed issue, or does HT need something more tailored?), whether the Spark-Build-Show structure still works with just one day monthly, who's presenting to the Board and what exactly we're asking for, and what the timeline looks like.

Let me get these answers first so I'm building toward the right outcome.Dobro, ovo mi daje jasnu sliku. Mjesečna frekvencija je pametniji početak — svaki PetAIk postaje "event" s težinom, ne rutina koja se razvodni. A HT-own pozicioniranje je hrabar ali obranjiv izbor.

Prije nego krenem u Board materijal, moram razumjeti još par stvari jer mijenjaju sadržajdecka:

**Zašto HT-own, a ne DT?** Board će to pitati. Koji je tvoj najjači argument — DT programi su preopćeniti? Prespori? Ne postoji grupni ekvivalent? Ili je logika "mi smo ispred, zašto čekati"?

**Mjesečna frekvencija mijenja arhitekturu dana.** Kad imaš samo 1 dan mjesečno, svaki mora biti ozbiljniji. Spark-Build-Show u 3 bloka i dalje drži, ali Build blok postaje kritičniji — ljudi moraju izaći s nečim opipljivim jer sljedeća prilika je za mjesec dana. Misliš li zadržati pola dana (4h) ili ići na cijeli dan kad je samo jednom mjesečno?

**Tko prezentira i što je "ask"?** Prezentiraš sam ili s nekim (HR, Fred)? I što konkretno tražiš od Boarda — zeleno svjetlo za pilot s X ljudi, budžet, ili samo awareness prije formalnog prijedloga?

**Timing?** Imaš li datum kad bi ovo trebalo biti spremno?

## Human  *(2026-04-02T20:08:12.844216+00:00)*

HT-own jer smo brzi i napredni; mjesečno 1 cijeli dan umjesto pola dana - razmisli i razradi strukturu dana, daj konkretne prijedloge za challenge i koga uključiti u dizajn istih; prezentiram ja sa par kolega (HR, CRO Marketing/Product, Strategy), pripremi nama prvo dokument za razradu i pripremu a kasnije ćemo doći do board materijala, ask je sponsorship i support; timing da krenemo s pilotom tokom Q2

## Assistant  *(2026-04-02T20:12:43.878680+00:00)*

Robi wants me to create a working document for the internal team (him + HR, CRO Marketing/Product, Strategy colleagues) to develop and prepare the PetAIk concept before it goes to the Board. This is an internal preparation document, not the Board deck itself.

Key inputs:
- HT-own because they're fast and advanced
- Monthly, 1 full day instead of half day
- Need to rethink the day structure for a full day
- Concrete challenge proposals
- Who to include in challenge design
- Presenting with HR, CRO Marketing/Product, Strategy colleagues
- First: preparation document for the team
- Later: Board materials

- Need sponsorship and support to pilot during Q2 2026

Now I'm working through how to structure a full eight-hour day. The Spark-Build-Show framework needs to expand significantly—I'm thinking roughly 90-120 minutes for an expanded Spark phase in the morning, then 3-4 hours for Build work in the middle, and wrapping with Show and Reflect in the late afternoon for another 90-120 minutes, accounting for breaks and lunch throughout.

For the working document itself, I need to think about what's realistic for the two participant profiles—Builders and Adopters—in this first pilot with the AI & Data Tribe and Sales/Marketing teams. Since this is meant for internal collaboration and will be shared across HR, Marketing, Product, and Strategy folks, I'll create it as a Word document rather than markdown, as that's more accessible for a non-technical audience.

Now let me build the working document. This is an internal prep document for Robi and his team (HR, CRO Marketing/Product, Strategy). It should be a Word doc since it's shared with non-technical colleagues.

Let me design the full-day structure carefully:

Full day = ~8 hours (say 9:00-17:00)

With monthly cadence, each day needs to be impactful. Here's my thinking:

**Morning:**
- 09:00-09:15 — Opening / Context setting (15 min)
- 09:15-10:30 — Spark block: Challenge brief, tool demo, inspiration (75 min)

- 10:30-10:45 — Break
- 10:45-11:00 — Team formation / challenge selection (15 min)

**Midday:**
- 11:00-13:00 — Build Block 1: Deep work (120 min)
- 13:00-13:45 — Lunch + informal networking

**Afternoon:**
- 13:45-15:15 — Build Block 2: Iteration & polish (90 min)
- 15:15-15:30 — Break
- 15:30-16:30 — Show block: Showcases (60 min)
- 16:30-17:00 — Closing / Wrap-up (30 min)

That breaks down to roughly 75 minutes for the spark phase, 3.5 hours of building split across two blocks with lunch in between, an hour for showcases, and 30 minutes to wrap up and document. For the challenges, I'm thinking about two distinct profiles: one for the AI & Data Tribe focused on building agentic workflows, benchmarking new tools, creating RAG prototypes, or developing AI-powered internal tools, and another for Sales/Marketing that includes automating reporting workflows and other marketing-specific applications.

I should loop in the AI & Data Tribe leads to validate technical feasibility, get input from the business units on what's actually relevant, and eventually bring in the AI Champions once they're identified. Now I'm structuring the full proposal document with sections covering the concept overview, the day's architecture, challenge options for the pilot, role definitions, the Q2 timeline, and key questions still to be resolved.

Writing the proposal document...

Good, docx is installed. Now let me create the document.

I noticed a syntax error - I have `[RIZIK] "` instead of `magenta("[RIZIK] ")` on one line. Let me fix that.

Now let me run the script.

Good, let me validate it.

The validate script must be elsewhere. Let me check.

Found it. Let me validate with the correct path.

The document passed validation. Let me copy it to the outputs folder and present it.

Now let me present the file.

The document is ready. Let me give Robi a summary of what I've produced and the key decisions I made.Evo radnog dokumenta. Ključne stvari koje sam razradio povrh Sonnetovog koncepta:

**Arhitektura dana — 8h umjesto 4h.** Pet blokova: Arrival (15 min) → Spark (75 min) → Build I & II (4h ukupno, prekinuto ručkom) → Show (60 min) → Reflect (30 min). BUILD je srce dana s 4 sata deep worka.

**Dva konkretna challengea za pilot.** PetAIk #1 je individualan ("Moj posao, ali s AI-em" — svatko automatizira svoj pain point), PetAIk #2 je timski (mješoviti A+B timovi na definiranom use caseu). Redoslijed je namjeran — prvo osobna relevantnost, pa kolaboracija.

**Dizajn tim za challengee** — 4 osobe (Tribe + Sales/Marketing + HR + budući AI Champion), sastanak 2 tjedna prije svakog PetAIk-a.

**Mjerenje bez ROI-ja** — output count, adoption rate, self-reported ušteda, NPS, plus kvalitativni materijal za Board story.

**9 otvorenih pitanja** na zadnjoj stranici — to je agenda za vaš prvi sastanak dizajn tima.

Pogledaj dokument i javi mi što treba promijeniti, dodati ili izbaciti prije nego ga pošalješ kolegama.

## Human  *(2026-04-02T20:12:47.961260+00:00)*

kreiraj mi interaktivnu html verziju tog radnog dokumenta

## Assistant  *(2026-04-02T20:16:52.677823+00:00)*

Robi wants an interactive HTML version of the working document. Let me read the frontend-design skill first to make sure I create something polished.

Now let me create an interactive HTML version of the PetAIk working document. This should be visually striking, with HT/Magenta branding, interactive elements like:
- Collapsible sections
- Progress tracking through sections
- Interactive checklist for open questions
- Smooth scrolling navigation
- Maybe a timeline for the pilot plan

Let me design something that feels like a modern internal tool/dashboard rather than a static document. The aesthetic should be clean, professional, with HT magenta as the accent color. I'll go for a refined, editorial feel.

Let me present the file.

Done. Let me give a brief summary.Evo interaktivne verzije. Ima bočnu navigaciju s aktivnim praćenjem sekcija, collapsible profile i challenge kartice, interaktivni checklist za otvorena pitanja s counterom, animacije na scroll, i mobile responsive dizajn. HT magenta je accent boja kroz cijeli dokument.

Interaktivni elementi: klikni na profile kartice i challenge kartice za expand/collapse, a otvorena pitanja na dnu možeš checkirati kao riješena.


---

# PetAIk koncept za HT organizaciju
- **Conversation ID:** `aca5bd26-5af2-49b1-a68d-b20319ec2a39`
- **Created:** 2026-04-02T19:57:48.178713+00:00
- **Updated:** 2026-04-02T20:02:13.166682+00:00
- **Messages:** 4

---

## Human  *(2026-04-02T19:57:49.852683+00:00)*

Ti si strateg, tehnolog, futurolog i organizacijski konzultant. Želimo uvesti novi koncept u HT-u, AI@Work day, kao svojevrsnu alternativu četverodnevnom radnom tjednu. Krenuli bismo možda jednom mjesečno, petkom pa skalirali na češće. Bitno mi je razraditi koncept, recimo da ga nazovemo "PetAIk", kako strukturirati takav program u tako velikoj organizaciji. Razmisli i postavi mi pitanja za dodatna pojašnjenja, nakon češ mi trebati za razradu koncepta razmišljajući pritom i o heterogenosti organizacije, front vs nonfront ljudi itd

## Assistant  *(2026-04-02T19:58:21.317414+00:00)*

Robi wants to develop a concept called "PetAIk" (clever wordplay - "Petak" = Friday in Croatian, + "AI") - an AI@Work day as an alternative to the 4-day work week at Hrvatski Telekom. He wants me to ask clarifying questions before developing the concept.

Let me think about the key dimensions I need to understand:

1. **Strategic intent** - is this about productivity, upskilling, culture, employer branding, or all of the above?
2. **Target population** - HT has ~1500-2000 employees, heterogeneous (front office: retail stores, call centers vs. non-front: corporate, tech, admin)

3. **Governance & rollout** - who owns it, how does it scale, what's the approval chain
4. **Measurement** - how do we know it worked?
5. **Content** - what happens on PetAIk day?
6. **Constraints** - labor law, collective agreements, customer-facing operations that can't just stop on Fridays

I need to ask sharp, executive-level questions that will help me build a solid concept.**PetAIk** — već sam naziv je zgodan jer funkcionira na dva nivoa (Petak + AI). Konceptualno jako zanimljivo kao alternativa 4-dnevnom tjednu — umjesto da *oduzimaš* dan, *transformiraš* ga.

Prije nego krenem u razradu, trebam razumjeti nekoliko ključnih dimenzija. Evo pitanja po skupinama:

---

**1. Strateška namjera — što je prava svrha?**

- Je li primarni cilj **upskilling** (podizanje AI pismenosti), **produktivnost** (daj ljudima prostor da automatiziraju vlastiti posao), **kulturu** (signalizirati da smo AI-first kompanija), ili **employer branding** (privući i zadržati talent)? Ili kombinacija — ako kombinacija, koji je prioritet?
- Je li PetAIk zamjena za nešto (npr. klasične edukacije, hackathone, petkom-popodne), ili potpuno novi sloj?

---

**2. Populacija i heterogenost**

- Kako gledaš na **front ljude** (retail, call centar) koji imaju shift-based rasporede i SLA obveze prema kupcima — misliš li da za njih PetAIk funkcionira kao rotacijski model, ili ih isključujemo u prvoj fazi?
- Postoji li već neka segmentacija u glavi (npr. najprije "white collar" populacija, pa skaliranje), ili inzistiraš na inkluzivnosti od starta?

---

**3. Format i sadržaj**

- Što se točno *događa* na PetAIk dan? Misliš li na **slobodan eksperimentalni prostor** (ljudi rade na AI projektima po volji), **strukturirani program** (radionice, challenges, learning sprints), ili **hibrid** (jutro strukturirano, poslijepodne slobodno)?
- Tko facilitira — AI & Data Tribe kao owner, HR, ili nešto treće?

---

**4. Mjerenje i legitimizacija**

- Kako ćeš opravdati Board/managementu da je taj dan "isplativ"? Imaš li već tezu o tome — output-based accountability, NPS zaposlenika, broj deployanih use caseova?
- Je li cilj da PetAIk eventualno postane **benefit** (= redukcija radnog vremena de facto), ili uvijek ostaje *radni dan, samo drugačije usmjeren*?

---

**5. Kontekst i ograničenja**

- Postoje li **kolektivni ugovor ili pravni okviri** koji ograničavaju fleksibilnost petka (HR / legal constraints)?
- Imaš li već saveznike u HR-u ili na Boardu, ili to trebaš još izgraditi kao ideju?
- Vremenski horizont — kad bi htio imati pilot spreman za prezentaciju, i pred kim?

---

Odgovori i na onoliko pitanja koliko ti je sada jasno — na temelju toga mogu razviti strukturirani koncept dokumenta, uključujući segmentacijski model, governance, sadržajni okvir i metriku.

## Human  *(2026-04-02T20:00:53.757326+00:00)*

1. primarni cilj je upskilling/reskilling, produktivnost i kultura; 2. volio bih inkluzivnost od starta, ali ne znam kako ju uvesti u front rolama koje su shift-based; 3. htio bih strukturirani eksperimentalni prostor, gdje ljudi uče i primjenjuju u isto vrijeme; 4. eventualno to bi mogao postati benefit, ali za prvu ruku trebam ideje, predloži mi nešto; 5. imam saveznike u HR-u i boardu, htio bih pilotirati čim prije pa skalirati

## Assistant  *(2026-04-02T20:02:13.149288+00:00)*

Robi has given me enough to work with. Let me now develop the full PetAIk concept. Let me think through this carefully.

Key parameters:
- Goals: upskilling/reskilling + productivity + culture (all three)
- Inkluzivnost from start, including front/shift roles (need creative solution)
- Structured experimental space (learn + apply simultaneously)
- Could become a benefit eventually
- Allies in HR and Board, wants to pilot ASAP

Let me think about the core concept and structure:

**Core Design Principles:**
1. Not a training day — a "build day" where learning happens through doing

2. Inclusive from day 1 — needs a front-role variant
3. Structured enough to produce outputs, free enough to feel different
4. Scalable governance model

For the front-role challenge, I'm considering a rotating time window that works around shift schedules — maybe a 3-4 hour block that moves through the week so everyone can participate under the same PetAIk banner, or alternatively, making content available on-demand so shift workers can engage during quieter periods, or even setting up a swap system where front employees can trade participation slots.

I could also station dedicated AI learning areas at retail locations where a portion of the team steps off the floor during PetAIk while others maintain coverage, keeping the Friday brand intact but letting front employees schedule their own floating PetAIk window within the month.

For the actual program structure, I'm thinking of a three-part day: a morning block focused on structured input like workshops or tool demos, a mid-day hands-on session where people immediately apply what they learned through projects, and an afternoon showcase where teams present their work — even rough drafts — to celebrate the effort. I'm also starting to think about how to segment participants based on their roles and experience levels. I'm mapping out the rollout timeline—starting with a single business unit that already has momentum from the Vibe Code Face-Off, then scaling through departments over six months. For the incentive layer, I'm weighing four benefit options: a bonus day off after hitting participation milestones, formal AI certification that accumulates from PetAIk hours, a personal portfolio approach tied to performance reviews, or flex-time banking where participation converts to flexible hours. Now I need to synthesize this into a coherent framework Robi can actually work with.Odlično. Imam dovoljno za razradu. Evo kompletnog konceptualnog okvira — namjerno ga strukturiram kao materijal koji možeš direktno koristiti za pilot prijedlog.

---

# PetAIk — Konceptualni okvir

## Osnovna filozofija

PetAIk nije edukacijski dan. Nije ni slobodan dan. To je **produkcijski dan budućnosti** — dan kad zaposlenici rade *na* poslu, a ne *u* poslu. Razlika je ključna za komunikaciju prema Board-u i zaposlenicima jednako.

Tagline prijedlog: **"Jedan dan za posao koji dolazi."**

---

## Tri cilja, jedan mehanizam

Umjesto da tretiraš upskilling, produktivnost i kulturu kao tri odvojena cilja, PetAIk ih rješava jednim dizajnom:

- **Upskilling** se događa jer ljudi uče alat rješavajući *vlastiti* problem
- **Produktivnost** se događa jer svaki PetAIk mora imati opipljivi output
- **Kultura** se gradi jer svi — od retail do C-suite — rade isto u isto vrijeme

Ovo je važno jer je jedina alternativa koja funkcionira u heterogenoj organizaciji ona gdje je **format različit, ali dignitet jednak**.

---

## Arhitektura dana — "3 bloka"

Vrijedi za sve segmente, uz adaptacije.

| Blok | Naziv | Trajanje | Što se događa |
|------|-------|----------|---------------|
| 1 | **Spark** | 90 min | Kratki strukturirani input — use case challenge, demo novog alata, ili "AI brief" koji definira što gradimo danas |
| 2 | **Build** | 120 min | Individualni ili timski rad — primjena alata na konkretan problem iz vlastitog posla |
| 3 | **Show** | 60 min | Kratki showcases — nedovršeno je OK, poanta je kultura dijeljenja pokušaja, ne samo uspjeha |

Ukupno: pola radnog dana. Ostatak petka = normalan rad ili po dogovoru s voditeljem.

---

## Segmentacija populacije — inkluzivnost bez naivnosti

Organizaciju dijeliš u 3 profila, ne po hijerarhiji nego po **načinu rada**:

**Profil A — Builders** (AI & Data Tribe, IT, arhitekti, developeri)
Format: tehnički challenge, sandbox environment, peer code/prompt review
Output: prototip, skript, novi pipeline, evaluacija alata

**Profil B — Adopters** (marketing, sales, finance, HR, legal, C-suite)
Format: no-code / low-code, prompt engineering, automatizacija vlastitih workaflowa
Output: prompt koji štedi X sati tjedno, automatiziran izvještaj, AI-assisted dokument

**Profil C — Front** (retail, call centar, terenski timovi)
Ovo je najdelikatniji problem. Rješenje:

> **"Floating PetAIk"** — Front zaposlenici ne rade PetAIk petkom, nego imaju **pravo na jedan AI dan unutar kalendarskog tjedna**, koji se dogovara s voditeljem smjene. Uvijek se zove PetAIk, brand je isti, sadržaj je prilagođen.

Konkretno za front:
- Kraći format — 2 sata, ne pola dana
- Mobile-first sadržaj (kratki AI challenge dostupan na mobitelu)
- Fokus na alate koji su im relevantni — AI za bilježenje call sažetaka, pripremu odgovora kupcu, pretragu KB-a
- Rotacijski raspored — u svakoj smjeni 20-30% tima je na PetAIk-u, ostatak pokriva

Ovo ti daje inkluzivnost bez operativnog kaosa i bez da front zaposlenici osjete PetAIk kao privilegij "onih gore".

---

## Governance model

**Central owner:** AI & Data Tribe (tvoj tim) — kurikulum, alati, challenge brief, mjerenje
**Co-owner:** HR — kultura, komunikacija, benefit layer, wellbeing kut
**Distribuirani izvršitelji:** AI Champion mreža

AI Champion je ključan element. Svaki odjel/tim nominira jednu osobu koja:
- Prima brief tjedan dana unaprijed
- Facilitira lokalni Build i Show blok
- Prijavljuje outpute centralnom timu
- Nije ekspert — to je feature, ne bug. Peer learning je snažniji od top-down edukacije.

---

## Pilot dizajn — "Start Small, Show Fast"

**Faza 0 — Priprema (2-3 tjedna):**
Odaberi 2 pilotna segmenta: AI & Data Tribe (Profil A, prirodni saveznik) + jedan business odjel koji već ima AI apetit — predlažem Sales/Marketing jer imaš momentum od Vibe Code Face-Off eventa.

**Faza 1 — Pilot (2 PetAIk-a, 2 petka):**
Mala skupina, 30-50 ljudi. Cilj nije savršenstvo — cilj je **story** koji možeš prenijeti Board-u. Dokumentiraj sve: što su napravili, koliko je trajalo, kako su se osjećali.

**Faza 2 — Evaluacija i prijedlog skaliranja (tjedan nakon drugog pilota):**
Prezentacija na Board-u s konkretnim outputima, NPS-om zaposlenika i prijedlogom za company-wide rollout.

**Faza 3 — Skaliranje (mjesec 2-3):**
Uvođenje AI Champion mreže, Floating PetAIk za front, standardizacija formata.

---

## Benefit layer — evolucija koncepta

Predlažem **tri razine evolucije** ovisno o tome koliko brzo organizacija sazrijeva:

**Razina 1 — Investicija u znanje** (odmah, pilot)
PetAIk je radni dan s posebnom namjenom. Nema de facto benefita osim smisla i učenja. Poruka: "HT investira tvoje radno vrijeme u tvoju budućnost."

**Razina 2 — AI Portfolio** (nakon 3-6 mjeseci)
Svaki zaposlenik gradi osobni AI Portfolio — dokumentirani outputi s PetAIk-a koji ulaze u razgovor o razvoju karijere i napredovanju. Ovo je benefit koji ne košta ništa ali ima visoku percipiranu vrijednost.

**Razina 3 — PetAIk Flex** (12+ mjeseci, ako kultura sazrije)
Zaposlenici koji su ostvarili X output-a na PetAIk-u dobivaju pravo na 1 slobodan dan kvartalno — de facto bonus slobodan dan. Ovo je najbliže 4-dnevnom tjednu, ali zasluženo i mjerljivo, ne automatsko.

---

## Kako opravdati Board-u

Izbjegni ROI računicu u ranoj fazi — preuranjeno i nepouzdano. Umjesto toga, idi s **tri argumenta:**

**1. Trošak neaktivnosti** — što košta da zaposlenici *ne* razvijaju AI kompetencije? Konkurencija, odljev talenata, zastarijevanje uloga.

**2. Benchmark** — sve veće telco i tech organizacije uvode slične formate (Google 20%, Microsoft AI Skills Initiative). HT može biti **prvi telco u regiji** koji formalizira AI dan.

**3. Pilot kao dokaz** — ne tražiš od Board-a da vjeruje konceptu, tražiš odobrenje za 2 petka s 50 ljudi. Rizik je minimalan, signal je ogroman.

---

## Što trebaš odmah

Da krenem u razradu konkretnih materijala, reci mi:

- Koji odjel/tim uz AI & Data Tribe ide u pilot — Sales, Marketing, HR?
- Trebam li ti pripremiti **pilot prijedlog za Board** (1-pager ili deck), **challenge brief za prvi PetAIk**, ili **AI Champion job description**?
- Ima li već datum na umu za prvi pilot petak?

