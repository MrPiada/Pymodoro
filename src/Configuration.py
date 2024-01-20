import yaml


class Configuration:
    def __init__(self, file_path):
        self.file_path = file_path
        with open(file_path, 'r') as yaml_file:
            config_data = yaml.safe_load(yaml_file)

            if 'timers' not in config_data or 'goals' not in config_data:
                raise ValueError("Incorrect YAML configuration file.")

            self.pauses = config_data.get('pauses', {})
            self.timers = config_data['timers']
            self.goals = config_data['goals']

            required_timers = [
                'pomodoro',
                'short_pause',
                'long_pause',
                'pause_ratio']
            required_goals = ['daily', 'weekly', 'monthly', 'yearly']
            self._check_required_elements(
                self.timers, 'timers', required_timers)
            self._check_required_elements(self.goals, 'goals', required_goals)

    def _check_required_elements(self, data, section_name, required_elements):
        for element in required_elements:
            if element not in data:
                raise ValueError(
                    f"L'attributo '{element}' è richiesto nella sezione '{section_name}'.")

    def save_to_yaml(self):
        config_data = {
            'pauses': self.pauses,
            'timers': self.timers,
            'goals': self.goals
        }

        with open(self.file_path, 'w') as yaml_file:
            yaml.dump(config_data, yaml_file, default_flow_style=False)
