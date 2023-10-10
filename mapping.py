cantus_mapping = {
    "properties": {
      "@id": {
        "type": "keyword"
      },
      "@type": {
        "type": "keyword"
      },
      "https://cantusdatabase.org/about/id-numbers/": {
        "type": "keyword"
      },
      "http://www.wikidata.org/prop/direct/P86": {
        "type": "nested",
        "properties": {
          "@id": {
            "type": "keyword"
          },
          "http://www.wikidata.org/entity/P2561": {
            "type": "keyword"
          }
        }
      },
      "https://schema.org/Dataset": {
        "type": "keyword"
      },
      "http://www.wikidata.org/entity/Q4484726": {
        "type": "keyword"
      },
      "http://www.wikidata.org/prop/direct/P136": {
        "type": "nested",
        "properties": {
          "@id": {
            "type": "keyword"
          },
          "http://www.wikidata.org/entity/P2561": {
            "type": "keyword"
          }
        }
      },
      "http://www.wikidata.org/prop/direct/P1922": {
        "type": "keyword"
      },
      "http://www.wikidata.org/entity/Q731978": {
        "type": "nested",
        "properties": {
          "@id": {
            "type": "keyword"
          },
          "http://www.wikidata.org/entity/P2561": {
            "type": "keyword"
          }
        }
      },
      "https://cantusdatabase.org/source/": {
        "type": "keyword"
      }
    }
  }


simssa_mapping = {
        "properties": {
            "@id": {"type": "keyword"},
            "@type": {"type": "keyword"},
            "http://www.wikidata.org/prop/direct/P86": {
                "type": "nested",
                "properties": {
                    "@id": {"type": "keyword"},
                    "http://www.wikidata.org/entity/P2561": {"type": "keyword"}
                }
            },
            "https://schema.org/Dataset": {"type": "keyword"},
            "https://db.simssa.ca/files/": {
                "type": "nested",
                "properties": {
                    "@id": {"type": "keyword"},
                    "@type": {"type": "keyword"},
                    "http://www.wikidata.org/prop/direct/P2701": {
                        "type": "nested",
                        "properties": {
                            "@id": {"type": "keyword"},
                            "http://www.wikidata.org/entity/P2561": {"type": "keyword"}
                        }
                    },
                    "Last_Pitch_Class": {"type": "float"}
                }
            },
            "http://www.wikidata.org/prop/direct/P135": {
                "type": "nested",
                "properties": {
                    "@id": {"type": "keyword"},
                    "http://www.wikidata.org/entity/P2561": {"type": "keyword"}
                }
            },
            "http://www.wikidata.org/prop/direct/P136": {
                "type": "nested",
                "properties": {
                    "@id": {"type": "keyword"},
                    "http://www.wikidata.org/entity/P2561": {"type": "keyword"}
                }
            },
            "http://www.wikidata.org/prop/direct/1476": {"type": "keyword"}
        }
    }


field_aliases = {
    "http://www.wikidata.org/prop/direct/P1476": "title",
    "http://www.wikidata.org/prop/direct/P86": "composer",
    "http://www.wikidata.org/prop/direct/P136": "genre",
    "http://www.wikidata.org/prop/direct/P826": "tonality",
    "http://www.wikidata.org/prop/direct/P2701": "file format",
    "http://www.wikidata.org/prop/direct/P577": "publication date",
    "http://www.wikidata.org/prop/direct/P2699": "URL",
    "http://www.wikidata.org/prop/direct/P50": "author",
    "http://www.wikidata.org/prop/direct/P175": "performer",
    "http://www.wikidata.org/prop/direct/P1545": "series ordinal",
    "http://www.wikidata.org/entity/Q4484726": "finalis",
    "http://www.wikidata.org/prop/direct/P2561": "name"
}

# Add field aliases to the mapping
for url, alias in field_aliases.items():
    if url in cantus_mapping["mappings"]["properties"]:
        cantus_mapping["mappings"]["properties"][alias] = cantus_mapping["mappings"]["properties"].pop(url)
        
