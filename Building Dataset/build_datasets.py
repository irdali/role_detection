from utilities import buildAllDatasets

if __name__ == '__main__':
    conditions = [[2.0, 0.5], [2.0, 1.0], [2.0, 1.5], [2.0, 2.0],
                  [1.5, 0.5], [1.5, 1.0], [1.5, 1.5], [1.5, 2.0],
                  [1.0, 0.5], [1.0, 1.0], [1.0, 1.5], [1.0, 2.0],
                  [0.5, 0.5], [0.5, 1.0], [0.5, 1.5], [0.5, 2.0]
              ]
    buildAllDatasets(conditions)