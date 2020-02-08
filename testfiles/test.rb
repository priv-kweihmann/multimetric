# frozen_string_literal: true

require 'json'
require 'pathname'

module SomeModule
  module Generator
    module Json
      class Simple
        def data
          {
            metadata: {
              rubycritic: {
                version: RubyCritic::VERSION
              }
            },
            analysed_modules: @analysed_modules,
            score: @analysed_modules.score
          }
        end

        def file_directory
          @file_directory ||= Pathname.new(Config.root)
        end

        def file_pathname
          Pathname.new(file_directory).join FILE_NAME
        end
      end
    end
  end
end
