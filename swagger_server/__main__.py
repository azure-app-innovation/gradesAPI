#!/usr/bin/env python3

import connexion

from swagger_server import encoder


def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Swagger DS/CS 519 Assessment - OpenAPI 3.0'}, pythonic_params=True)

    @app.route('/')
    def starting_url():
        return "OK"

    app.run(port=8000)
    
if __name__ == '__main__':
    main()
