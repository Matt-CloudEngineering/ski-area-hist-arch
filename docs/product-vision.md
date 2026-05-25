# Fantasy Shred Product Vision

Fantasy Shred is evolving from a ski-area historical archive into a lifetime ski and snowboard history platform.

## Core Idea

A user should be able to build a lifelong personal repository of every ski and snowboard day across the world.

The platform should combine:

- resorts visited
- dates ridden/skied
- trails and lifts used
- vertical feet and acreage context
- weather conditions for each trip
- historical resort metadata
- map and trail evolution
- pass activity from Ikon, Epic, and other providers
- personal media, notes, and milestones

## Public Knowledge Layer

The public archive supports every user's personal history by maintaining structured resort intelligence:

- resort name and location
- official website
- operating status
- ownership model
- current vertical feet
- current skiable acreage
- trail count
- lift count
- historical trail maps
- resort timeline
- expansion history
- state/private/corporate ownership
- archival source links
- county, town, library, and state archive references

## Personal History Layer

Each user can build a private or shareable history of ski/board days.

Potential user objects:

- seasons
- trips
- ski days
- resorts
- lifts ridden
- trails ridden
- weather snapshots
- snowfall conditions
- companions
- photos/videos
- notes
- gear used
- pass product used
- milestones

## Key Product Differentiator

Fantasy Shred should answer questions like:

- Where did I ski most this season?
- What was my best powder day?
- Which resort had the coldest day I skied?
- How many vertical feet did I ski across my lifetime?
- How many Ikon/Epic resorts have I visited?
- What trails have I repeated most?
- How did the resort look historically when I visited?
- What was the weather and snowfall on each trip?

## Pass Import Strategy

The highest-value onboarding flow is automated or semi-automated import from major pass ecosystems.

Priority sources:

1. Ikon Pass
2. Epic Pass
3. Mountain Collective
4. Indy Pass
5. Resort-specific RFID/pass portals
6. User-uploaded CSV/PDF/screenshots
7. Manual trip entry

If official APIs are unavailable, support:

- CSV imports
- account export files
- email receipt parsing
- screenshot/OCR parsing
- browser-assisted user uploads
- manual correction workflows

## Weather Enrichment

Every ski day should be enriched with archival weather data.

Potential weather fields:

- high temperature
- low temperature
- precipitation
- snowfall
- wind speed
- wind gusts
- cloud cover
- freeze/thaw status
- snow depth if available
- nearest weather station
- source confidence

Weather enrichment should be reproducible and source-linked.

Potential sources:

- NOAA
- National Weather Service
- Open-Meteo historical API
- resort snow reports
- SNOTEL where regionally applicable
- local mountain weather archives

## Long-Term Platform Shape

```text
Fantasy Shred
├── Public Resort Archive
├── Personal Ski/Board Logbook
├── Pass Import System
├── Historical Weather Enrichment
├── Trail/Map History Explorer
├── Season Recaps
├── Lifetime Stats
├── Social/Shareable Profiles
└── AI Trip Memory Search
```

## Strategic Positioning

Fantasy Shred should become the skier and snowboarder's personal lifetime archive: part logbook, part historical resort atlas, part season recap engine, and part AI-enhanced ski memory system.
