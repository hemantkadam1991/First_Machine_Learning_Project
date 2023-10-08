from collections import namedtuple


DataIngestionConfig = namedtuple("DataIngestionConfig", 
["dataset_download_url","tgz_download_dir","raw_data_dir","ingested_train_dir", "ingested_test_dir"])

DataValidationConfig = namedtuple("DataValidationConfig", ["schema_file_path"])

DataTransformtionConfig = namedtuple("DataTransformtionConfig", 
["add_bedroom_per_room","transformed_train_dir","transformed_test_dir","preprocessed_object_file_path"])

ModelTrainerConfig = namedtuple("ModelTrainerConfig", ["trained_model_filepath", "base_accuracy"]) 

ModelEvaluationConfig = namedtuple("ModelEvaluationConfig", ["Model_Evaluation_filepath", "time_stamp"])

ModelPusherConfig = namedtuple("ModelPusherConfig", ["export_dir_path"]) 