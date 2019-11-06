#! /usr/bin/env python


imp



with beam.Pipeline(options=options) as p:

    # Read from PubSub into a PCollection.
    lines = p | beam.io.ReadStringsFromPubSub(topic=known_args.input_topic)

    # Group and aggregate each JSON object.
    transformed = (lines
                   | 'Split' >> beam.FlatMap(lambda x: x.split("\n"))
                   | 'jsonParse' >> beam.ParDo(jsonParse())
                   | beam.WindowInto(window.FixedWindows(15,0))
                   | 'Combine' >> beam.CombinePerKey(sum))

    # Create Entity.
    transformed = transformed | 'create entity' >> beam.Map(
      EntityWrapper(config.NAMESPACE, config.KIND, config.ANCESTOR).make_entity)

    # Write to Datastore.
    transformed | 'write to datastore' >> WriteToDatastore(known_args.dataset_id)

