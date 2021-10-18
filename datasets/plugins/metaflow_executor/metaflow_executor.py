from datasets.dataset import ProgramExecutor


class MetaflowExecutor(ProgramExecutor):
    @property
    def run_id(self) -> str:
        from metaflow import current

        return current.run_id

    @property
    def datastore_path(self) -> str:
        from metaflow import current
        from metaflow.datastore import MetaflowDataStore

        datastore: MetaflowDataStore = current.flow._datastore
        return datastore.get_datastore_root_from_config(print)

    @property
    def program_name(self) -> str:
        from metaflow import current

        return current.flow_name

    @property
    def context(self) -> str:
        return "offline"
