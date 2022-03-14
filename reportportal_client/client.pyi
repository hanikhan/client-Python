from requests import Session
from typing import Any, Dict, List, Optional, Text, Tuple, Union
from reportportal_client.core.log_manager import LogManager as LogManager
from reportportal_client.core.rp_issues import Issue as Issue


def current() -> RPClient: ...


class RPClient:
    _log_manager: LogManager = ...
    api_v1: Text = ...
    api_v2: Text = ...
    base_url_v1: Text = ...
    base_url_v2: Text = ...
    endpoint: Text = ...
    is_skipped_an_issue: bool = ...
    launch_id: Text = ...
    log_batch_size: int = ...
    project: Text = ...
    token: Text = ...
    verify_ssl: bool = ...
    session: Session = ...
    def __init__(self,
                 endpoint: Text,
                 project: Text, token: Text,
                 log_batch_size: int = ...,
                 is_skipped_an_issue: bool = ...,
                 verify_ssl: bool = ...,
                 retries: int = ...,
                 max_pool_size: int = ...,
                 launch_id: Text = ...) -> None: ...
    def finish_launch(self,
                      end_time: Text,
                      status: Text = ...,
                      attributes: Optional[Union[List, Dict]] = ...,
                      **kwargs: Any) -> Dict: ...
    def finish_test_item(self,
                    item_id: Text,
                    end_time: Text,
                    status: Text,
                    issue: Optional[Issue] = ...,
                    attributes: List = ...,
                    **kwargs: Any) -> None: ...
    def get_item_id_by_uuid(self, uuid: Text) -> Text: ...
    def get_launch_info(self) -> Dict: ...
    def get_launch_ui_id(self) -> Optional[Dict]: ...
    def get_launch_ui_url(self) -> Text: ...
    def get_project_settings(self) -> Dict: ...
    def log(self,
            time: Text,
            message: Text,
            level: Optional[Union[int, Text]] = ...,
            attachment: Optional[Dict] = ...,
            item_id: Optional[Text] = ...) -> None: ...
    def start_launch(self,
                     name: Text,
                     start_time: Text,
                     description: Text = ...,
                     attributes: Optional[Union[List, Dict]] = ...,
                     mode: Text = ...,
                     rerun: bool = ...,
                     rerun_of: Text = ...,
                     **kwargs: Any) -> Text: ...
    def start_test_item(self,
                   name: Text,
                   start_time: Text,
                   item_type: Text,
                   description: Text = ...,
                   attributes: Optional[Union[List, Dict]] = ...,
                   parameters: Dict = ...,
                   parent_item_id: Text = ...,
                   has_stats: bool = ...,
                   code_ref: Text = ...,
                   **kwargs: Any) -> Text: ...
    def terminate(self, *args: Tuple, **kwargs: Any) -> None: ...
    def update_test_item(self, item_uuid: Text, attributes: Optional[Union[List, Dict]], description: Optional[Text]):
