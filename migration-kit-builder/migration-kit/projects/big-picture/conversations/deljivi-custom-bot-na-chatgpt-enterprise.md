# Deljivi custom bot na ChatGPT Enterprise
- **Conversation ID:** `da48f6fc-41f1-4ae0-90b7-471537eca435`
- **Created:** 2026-04-04T09:49:51.811373+00:00
- **Updated:** 2026-04-04T09:58:51.306405+00:00
- **Messages:** 8

---

## Human  *(2026-04-04T09:49:52.136306+00:00)*

Htio bih kreirati custom bota na ChatGPT Enterprise kojem želim da mogu pristupiti svi kolege (uključujući one koji nemaju licencu), kako sa to napravim?

## Assistant  *(2026-04-04T09:50:19.563895+00:00)*

The user is asking about creating a custom bot on ChatGPT Enterprise that can be accessed by all colleagues, including those without a license. Let me search for current information on this.

Let me search more specifically about sharing custom GPTs with people who don't have a license/seat in the Enterprise workspace.

Based on the search results, it's clear that ChatGPT Enterprise requires users to have a seat (license) in the workspace to access custom GPTs. There's no native way to share a custom GPT with colleagues who don't have an Enterprise seat. Let me provide a clear answer.Robi, kratki odgovor: **to nativno nije moguće.** Custom GPTs u ChatGPT Enterprise mogu koristiti samo članovi koji imaju seat (licencu) u vašem workspace-u.

Evo opcija koje imaš:

**Dijeljenje unutar workspace-a** — u Enterprise workspace-u možeš podesiti razine dijeljenja GPT-ova: privatno, samo po pozivu, unutar workspace-a, ili šire — ali to sve zahtijeva da korisnik bude član workspace-a. Korisnici moraju biti prijavljeni da bi započeli razgovor s GPT-om.

**Opcije za kolege bez licence:**

1. **Dodati im seat** — najjednostavnije rješenje, ali košta. Enterprise sada ima i Codex-only seatove koji su usage-based bez fiksnog mjesečnog troška, ali ti daju samo Codex pristup, ne ChatGPT. Za GPT pristup trebaju standardni ChatGPT seatovi.

2. **Objaviti GPT javno (GPT Store)** — GPT se može objaviti javno ako je eligible, ali tada ga mogu koristiti svi, ne samo kolege, i gubi se Enterprise data privacy.

3. **Izgraditi vlastiti frontend preko OpenAI API-ja** — ovo je najfleksibilniji pristup. Koristiš Assistants API s istim instrukcijama i knowledge base-om kao tvoj custom GPT, a napraviš jednostavan web interface (poput onog subtitle toola koji si već napravio). Tako kontroliraš pristup, a kolegama ne treba ChatGPT licenca.

S obzirom na tvoje iskustvo s browser-based toolovima i Claude API-jem, opcija 3 ti je vjerojatno najprirodnija — isti princip, samo s OpenAI Assistants API. Želiš li da ti pomognem strukturirati takav pristup?

## Human  *(2026-04-04T09:51:06.015041+00:00)*

A je li nešto slično moguće sa NotebookLM i Gemini Enterprise?

## Assistant  *(2026-04-04T09:51:24.127306+00:00)*

The user is asking about whether something similar is possible with NotebookLM and Gemini Enterprise - specifically sharing custom bots/agents with colleagues who don't have a license.

Good, I have enough information now. Let me summarize the situation for NotebookLM Enterprise and Gemini Enterprise.Ista priča, Robi — i tu je licenca obavezna za pristup.

**NotebookLM Enterprise:** Notebooke možeš dijeliti s kolegama, ali oni moraju imati NotebookLM Enterprise ili Gemini Enterprise licencu. Dodatno, korisnici moraju biti u istom Google Cloud projektu i imati dodijeljenu Cloud NotebookLM User IAM rolu.

**NotebookLM kao Workspace core service:** NotebookLM i NotebookLM Plus su sada uključeni kao core servisi za Workspace Business i Enterprise korisnike, što znači da kolege s Workspace licencom automatski dobivaju pristup — ali opet, trebaju licencu.

**Public sharing postoji, ali nije opcija za enterprise:** Javno dijeljenje notebooka je omogućeno samo za osobne (consumer) račune — trenutno je onemogućeno za Workspace Enterprise ili Education račune.

Dakle, zaključak je isti kao kod ChatGPT Enterprise — nativno ne možeš dati pristup kolegama bez licence. Alternativa je opet ista: izgraditi vlastiti frontend koristeći Gemini API (Vertex AI), čime kontroliraš tko pristupa, bez potrebe za individualnim licencama.

S obzirom da ste na GCP-u s Plutom, Vertex AI vam je već blizu — mogao bi biti čak elegantniji put nego OpenAI API rješenje. Želiš da razradimo taj pristup?

## Human  *(2026-04-04T09:51:49.062592+00:00)*

Razradi

## Assistant  *(2026-04-04T09:52:29.426445+00:00)*

Robi wants me to elaborate on building a custom frontend using Vertex AI/Gemini API as an alternative to requiring individual licenses for ChatGPT Enterprise or NotebookLM Enterprise. Given his context - he's on GCP with Pluto, has experience building browser-based tools (the subtitle tool), and leads the AI & Data Tribe at HT - I should provide a concrete, actionable architecture.

Let me think about what would be most useful:

1. Architecture overview - how to build a custom "bot" accessible to all colleagues
2. Key components: Gemini API via Vertex AI, knowledge base/RAG, simple web frontend, authentication

3. Now I'm considering the practical constraints specific to HT - leveraging their existing GCP infrastructure, integrating with corporate authentication systems, and ensuring data privacy compliance. I should frame this as a concrete implementation plan rather than generic guidance, and decide whether to offer a structured document or keep it conversational for mobile readability.OK, evo konkretnog pristupa za HT kontekst.

## Koncept

Umjesto da kupuješ licencu svakom korisniku, gradiš **internu web aplikaciju** koja koristi Gemini API (ili OpenAI API) na backendu, a korisnicima izlaže jednostavan chat interface. Ti kontroliraš instrukcije, knowledge base i pristup — kolege vide samo chat.

## Arhitektura

**Frontend** — jednostrana web aplikacija (React ili čisti HTML/JS, kao tvoj subtitle tool). Hostas je interno na GCP-u (Cloud Run ili App Engine). Kolege pristupaju preko browsera, bez ikakve instalacije.

**Autentikacija** — HT korporativni SSO (SAML/OIDC). Ako koristite Google Workspace ili Azure AD, to je straightforward integracija s Cloud Run. Time kontroliraš tko pristupa — svi s HT računom, ili samo određene grupe.

**Backend** — tanka API layer (Python Flask/FastAPI ili Node.js) koji:
- Prima korisnikov upit
- Dodaje system prompt (tvoje custom instrukcije — ekvivalent "GPT instructions")
- Opcionalno radi RAG: vuče relevantne dokumente iz knowledge base-a i dodaje ih u kontekst
- Šalje sve na Vertex AI Gemini API
- Vraća odgovor korisniku

**Knowledge base (RAG)** — za ekvivalent NotebookLM-ovog "grounding on sources", imaš nekoliko opcija:
- **Vertex AI Search** — najbrži put, uploadas dokumente, Google ih indeksira i automatski radi retrieval. Managed, minimalan kod.
- **Custom RAG na Pluto infrastrukturi** — embeddings u BigQuery ili AlloyDB, veća kontrola ali više posla.
- **Jednostavno**: za manji set dokumenata, možeš ih čak stuffati direktno u context window (Gemini 2.5 Pro ima 1M tokena).

## Troškovi vs. licence

Gemini API preko Vertex AI se plaća po tokenima — za interni alat s recimo 50-100 korisnika koji dnevno pošalju po 10-20 upita, govorimo o redu veličine $100-500/mj, ovisno o modelu. To je dramatično jeftinije od 50+ Enterprise licenci.

## Praktični koraci

1. **PoC (1-2 dana)** — napravi minimalni chat UI + FastAPI backend koji poziva Gemini API s hardkodiranim system promptom. Deployaj na Cloud Run. Ovo možeš čak i sam napraviti po istom principu kao subtitle tool.

2. **Dodaj RAG (3-5 dana)** — integriraj Vertex AI Search s tvojim dokumentima (npr. interni pravilnici, prodajni materijali, FAQ).

3. **Dodaj auth (1 dan)** — Cloud Run + IAP (Identity-Aware Proxy) za SSO. Nema potrebe za custom auth kodom.

4. **Skaliraj** — dodaj logiranje razgovora, analytics, multiple "botove" (različiti system prompti za različite use case-ove).

## Zašto je ovo bolji pristup od licenci

- Plaćaš po korištenju, ne po sjedalici
- Potpuna kontrola nad instrukcijama, izvorima i pristupom
- Data ostaje na vašem GCP-u — nema slanja u OpenAI/Google consumer produkte
- Možeš imati više specijaliziranih botova (HR bot, Sales bot, IT support bot) na istoj infrastrukturi
- Uklapa se u governance model koji gradiš s Fredom — ovo je upravo taj "agentic framework" u praksi

Želiš da ti napravim detaljniji tehnički blueprint kao dokument, ili da skiciramo konkretan PoC kod?

## Human  *(2026-04-04T09:53:48.348995+00:00)*

Napravi tehnički blueprint, zvat će se Big Picture assistant

## Assistant  *(2026-04-04T09:58:51.293360+00:00)*

The user wants me to create a technical blueprint document for the "Big Picture Assistant" - an internal AI chat application for HT. Let me read the relevant skill files first to determine the best format.

Given this is a technical blueprint document, I should consider whether to make it as a docx, PDF, HTML, or markdown. The user said "tehnički blueprint" - this seems like it should be a professional document. Let me check the docx skill since this seems like it could be a formal deliverable.

Actually, let me think about this. The user is on mobile and asked for a technical blueprint. This is a substantial document that should be a formal deliverable. 

I'll pull up the docx skill to build out a proper Word document for this.

Now let me create a comprehensive technical blueprint document for the "Big Picture Assistant" as a Word document. This is a formal deliverable that Robi can share with his team and potentially present to the Board or Fred.

Network is disabled. Let me check if docx is already installed.

Good, docx is already installed. Let me create the technical blueprint document now.

Let me run the script to generate the docx.

Let me validate the document.

Validation passed. Let me copy to outputs and present.

Done. Let me present the file.

Document is ready.Evo blueprinta. Dokument pokriva 11 sekcija: od executive summary-ja i problem statementa, preko detaljne arhitekture (IAP auth, FastAPI backend, Vertex AI Search RAG), bot management sustava s 5 inicijalnih botova, cost modela s usporedbom licence vs. API, do 4-faznog implementacijskog plana (PoC za 2 tjedna) i governance okvira.

Namjerno sam uključio alignment s Fredom i joint governance modelom u "Sljedeće korake" — tako ti dokument može služiti i kao podloga za taj razgovor.
