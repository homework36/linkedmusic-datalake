updated_mapping = {
    "mappings": {
        "properties": {
            "@id": {"type": "text"},
            "@type": {"type": "text"},
            "Dataset": {"properties": {"@id": {"type": "text"}}},
            "P135": {
                "type": "nested",
                "properties": {
                    "@id": {"type": "text"},
                    "P2561": {
                        "type": "nested",
                        "properties": {
                            "@value": {"type": "text"}
                        }
                    }
                }
            },
            # "movement": {"type": "alias", "path": "P135.P2561.@value"},
            "P136": {
                "type": "nested",
                "properties": {
                    "@id": {"type": "text"},
                    "@value": {"type": "text"},
                    "P2561": {
                        "type": "nested",
                        "properties": {
                            "@value": {"type": "text"}
                        }
                    }
                }
            },
            # "genre": {"type": "alias", "path": "P136.P2561.@value"},
            "P1476": {"properties": {"@value": {"type": "text"}}},
            "title": {"type": "alias", "path": "P1476.@value"},
            "P1922": {"properties": {"@value": {"type": "text"}}},
            "first line": {"type": "alias", "path": "P1922.@value"},
            "P86": {
                "type": "nested",
                "properties": {
                    "@id": {"type": "text"},
                    "P2561": {
                        "type": "nested",
                        "properties": {
                            "@value": {"type": "text"}
                        }
                    }
                }
            },
            # "composer": {"type": "alias", "path": "P86.P2561.@value"},
            "Q4484726": {"properties": {"@value": {"type": "text"}}},
            "final": {"type": "alias", "path": "Q4484726.@value"},
            "Q731978": {
                "type": "nested",
                "properties": {
                    "@id": {"type": "text"},
                    "@value": {"type": "text"},
                    "P2561": {
                        "type": "nested",
                        "properties": {
                            "@value": {"type": "text"}
                        }
                    }
                }
            },
            # "mode": {"type": "alias", "path": "Q731978.P2561.@value"},
            "files": {
                "type": "nested",
                "properties": {
                    "@id": {"type": "text"},
                    "@type": {"type": "text"},
                    "P2701": {
                        "type": "nested",
                        "properties": {
                            "@id": {"type": "text"},
                            "P2561": {
                                "type": "nested",
                                "properties": {
                                    "@value": {"type": "text"}
                                }
                            }
                        }
                    },
                    # "file format": {"type": "alias", "path": "files.P2701.P2561.@value"}
                }
            },
            "id-numbers": {"properties": {"@id": {"type": "text"}}},
            "source": {"properties": {"@id": {"type": "text"}}}
        }
    }
}
