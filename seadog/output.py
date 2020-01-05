import os
import click
import tempfile

class Output:
    def png(output, image):
        # TODO: handle this in chunks?
        if output == None:
            Output.eog(image)
            return
        output.write(image)
        output.flush()

    def eog(image):
        fd, path = tempfile.mkstemp()
        with os.fdopen(fd, 'w+b') as tmp:
            tmp.write(image)
            click.launch(path)

    def csv(output, dataframe):
        # TODO: handle this in chunks?
        output_csv = dataframe.to_csv()
        output.write(output_csv.encode('utf-8'))
        output.flush()